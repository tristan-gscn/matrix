# Écrire du Python "en vrai" en Rust : le guide

Ce cours explique la mécanique derrière l'architecture de ce projet :
`Vector` et `Matrix` sont des classes Python, mais leur implémentation réelle
vit en Rust. On part de zéro (une simple fonction) puis on reconstruit,
étape par étape, ce qui a été fait dans ce dépôt.

## 1. Ce qu'on essaie de faire, concrètement

Python (CPython, l'implémentation de référence) est lui-même écrit en C.
Chaque `def`, chaque `class`, chaque `list` est en réalité une structure C
manipulée via l'**API C de Python** (`Python.h`). N'importe quel langage
capable de produire une bibliothèque partagée (`.so` sur Linux, `.pyd` sur
Windows) respectant cette API peut donc fournir un "module Python" — c'est
comme ça que numpy, par exemple, expose ses tableaux.

Écrire cette API C à la main est pénible et dangereux (gestion manuelle du
refcounting, risques de segfault). **PyO3** est une bibliothèque Rust qui
génère cette glue pour vous : vous écrivez du Rust normal avec quelques
macros (`#[pyclass]`, `#[pymethods]`, `#[pymodule]`), et PyO3 produit le code
C-API équivalent. **maturin** est l'outil qui compile ce crate Rust et
l'empaquette en wheel Python installable.

La chaîne complète :

```
votre code Rust  --(macros PyO3)-->  code C-API  --(cargo, compilateur Rust)-->  libxxx.so
                                                                                     |
                                                                    import xxx  <---'  (CPython charge le .so)
```

## 2. Outillage minimal

- `cargo` / `rustc` : compilateur Rust (déjà présents si `cargo --version` répond).
- `pyo3` : crate à ajouter en dépendance Rust.
- `maturin` : build-backend PEP 517, invoqué automatiquement par `uv`/`pip`
  lors de l'installation du projet, puisque `pyproject.toml` le déclare.

Aucune installation manuelle de maturin n'est nécessaire : `uv sync` le
télécharge tout seul dans un environnement isolé, exactement comme il le
ferait pour n'importe quel autre `build-backend`.

## 3. L'exemple le plus simple possible : une fonction

Avant les classes, voyons le cas le plus simple : exposer une **fonction**
Rust comme fonction Python. Un mini-crate `demo/` ressemblerait à :

```toml
# demo/Cargo.toml
[package]
name = "demo"
edition = "2021"

[lib]
name = "demo"                      # nom du module importable : `import demo`
crate-type = ["cdylib"]

[dependencies]
pyo3 = { version = "0.22", features = ["extension-module"] }
```

```toml
# demo/pyproject.toml
[build-system]
requires = ["maturin>=1.5,<2.0"]
build-backend = "maturin"

[project]
name = "demo"
requires-python = ">=3.11"
```

```rust
// demo/src/lib.rs
use pyo3::prelude::*;

/// La fonction qu'on veut exposer à Python.
#[pyfunction]
fn add(a: f64, b: f64) -> f64 {
    a + b
}

/// Le point d'entrée : déclare ce que le module Python `demo` contient.
#[pymodule]
fn demo(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    Ok(())
}
```

Une fois compilé et installé (`maturin develop`, ou via `uv`/`pip install`),
côté Python :

```python
>>> import demo
>>> demo.add(2.0, 3.0)
5.0
```

**C'est tout le principe.** Une classe n'est qu'une extension de cette même
idée : au lieu d'exposer une fonction, on expose une structure et ses
méthodes.

## 4. Passer à une classe : `#[pyclass]` / `#[pymethods]`

C'est exactement ce que fait `src/rust/vector/mod.rs` :

```rust
use pyo3::prelude::*;

#[pyclass(subclass)]          // ← transforme une struct Rust en classe Python
pub struct Vector {
    pub data: Vec<f64>,
}
```

- `#[pyclass]` génère le type Python (son `tp_name`, son allocation mémoire,
  etc.).
- `subclass` autorise du code Python à hériter de cette classe. Ce projet ne
  s'en sert plus (`Vector`/`Matrix` sont directement les classes Rust, sans
  sous-classe Python), mais l'option reste inoffensive à garder si un besoin
  de ce genre apparaît plus tard.

Les méthodes vont dans un bloc séparé, annoté `#[pymethods]` :

```rust
// src/rust/vector/core/new.rs
use pyo3::prelude::*;
use crate::vector::Vector;

#[pymethods]
impl Vector {
    #[new]                          // ← correspond à __init__ / __new__
    fn new(data: Vec<f64>) -> Self {
        Vector { data }
    }
}
```

`#[new]` marque le constructeur : `Vector([1.0, 2.0])` côté Python appelle
cette fonction. Notez que Rust convertit **automatiquement** une liste
Python de flottants en `Vec<f64>` : c'est le rôle du trait
`FromPyObject`, que PyO3 implémente pour la plupart des types standards
(nombres, `String`, `Vec<T>`, `HashMap`, tuples...). Vous n'écrivez jamais
cette conversion vous-même pour les cas simples.

### Les méthodes spéciales ("dunder")

Elles se déclarent exactement comme en Python, juste avec des types Rust :

```rust
// src/rust/vector/core/len.rs
#[pymethods]
impl Vector {
    fn __len__(&self) -> usize {
        self.data.len()
    }
}
```

```rust
// src/rust/vector/core/getitem.rs
#[pymethods]
impl Vector {
    fn __getitem__(&self, index: isize) -> PyResult<f64> {
        normalize_index(index, self.data.len())
            .map(|i| self.data[i])
            .ok_or_else(|| PyIndexError::new_err("vector index out of range"))
    }
}
```

Deux choses à retenir ici :

1. **Les erreurs sont des valeurs.** Une fonction qui peut échouer retourne
   `PyResult<T>` (= `Result<T, PyErr>`). Retourner `Err(PyIndexError::new_err(...))`
   revient exactement à faire `raise IndexError(...)` en Python.
2. **Rien n'est automatique pour les indices négatifs** — `Vec<T>` de Rust
   ne comprend pas `v[-1]`. Il faut le réimplémenter à la main (fonction
   `normalize_index` dans `src/rust/utils.rs`) ; c'est le genre de détail
   "gratuit" en Python pur qui a un coût dès qu'on redescend au niveau
   d'une structure de données brute.

## 5. Le module : point d'entrée unique

Toutes les classes doivent être enregistrées dans une fonction annotée
`#[pymodule]` :

```rust
// src/rust/lib.rs
#[pymodule]
fn _core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Vector>()?;
    m.add_class::<VectorIter>()?;
    m.add_class::<Matrix>()?;
    Ok(())
}
```

Le nom de cette fonction (`_core`) doit correspondre au `module-name`
déclaré dans `pyproject.toml` (`matrix._core`) — voir section 8 : c'est ce
qui permet à l'extension compilée de se comporter comme un sous-module
interne du paquet Python `matrix`, plutôt que comme un paquet séparé.

## 6. Découper en plusieurs fichiers

Contrairement à Python, Rust autorise plusieurs blocs `impl` pour le même
type, y compris dans des fichiers différents — à condition d'activer la
feature `multiple-pymethods` de PyO3 :

```toml
# Cargo.toml
pyo3 = { version = "0.22", features = ["extension-module", "multiple-pymethods"] }
```

Sans elle, un deuxième `#[pymethods] impl Vector { ... }` dans un autre
fichier provoquerait une erreur de compilation (PyO3 utilise un mécanisme
d'inventaire global par type, qui doit être explicitement autorisé à
recevoir plusieurs contributions). Une fois la feature activée, la struct
et chaque méthode peuvent vivre dans leur propre fichier, reliés par un
`mod.rs` qui déclare les sous-modules. Le projet pousse même le découpage
un cran plus loin, avec un sous-dossier par "famille" de fonctionnalité :

```
src/rust/vector/
  mod.rs          -- struct Vector, `mod core;` (`mod ex00;` etc. à venir)
  core/           -- base : new, copy, len, getitem, iter, eq, repr
  ex00/           -- add, sub, scl (et ainsi de suite, un dossier par exercice)
```

Un piège classique : une méthode définie dans un fichier et utilisée dans
un autre (ex. `shape()` appelée depuis `eq.rs`) doit être marquée `pub`,
sinon Rust la considère privée au module qui la déclare.

Autre piège lié au découpage : les imports doivent utiliser des chemins
absolus (`crate::vector::Vector`, `crate::matrix::Matrix`) plutôt que
`super::`, pour rester valides quelle que soit la profondeur d'imbrication
des sous-dossiers.

## 7. Le piège de l'héritage : `Self` ne suit pas la sous-classe Python

*(Pertinent si vous réintroduisez `#[pyclass(subclass)]` avec une vraie
sous-classe Python un jour — ce projet n'en a plus besoin aujourd'hui,
mais le piège reste bon à connaître.)*

Quand une méthode Rust retourne `Self` (ex. `copy(&self) -> Self`), et
qu'elle est appelée depuis une **sous-classe Python** de cette classe
Rust, PyO3 construit un nouvel objet du type Rust de base — jamais de la
sous-classe réelle. La correction consiste à ne jamais supposer le type
statique de `Self`, mais à demander à Python quel est le **vrai type
dynamique** de l'instance, et à le rappeler comme un constructeur :

```rust
fn copy(slf: &Bound<'_, Self>) -> PyResult<PyObject> {
    let data = slf.borrow().data.clone();
    slf.get_type().call1((data,)).map(Bound::unbind)
}
```

`slf.get_type()` récupère le type Python réel de l'instance (qui peut être
une sous-classe), et `.call1((data,))` l'appelle comme `type(self)(data)`
le ferait en Python.

## 8. Un seul projet : Python et Rust dans le même `src/`

Contrairement à un crate PyO3/maturin "classique" (un paquet séparé), ce
projet est un **projet maturin en mode mixte** : un seul `pyproject.toml`,
un seul `Cargo.toml`, et un seul dossier `src/` qui contient à la fois le
code Rust et le code Python.

```toml
# pyproject.toml
[build-system]
requires = ["maturin>=1.5,<2.0"]
build-backend = "maturin"

[tool.maturin]
python-source = "src"      # `src/matrix/` est le paquet Python
module-name = "matrix._core"  # l'extension compilée est un sous-module
```

```toml
# Cargo.toml
[lib]
name = "_core"
path = "src/rust/lib.rs"   # la racine du crate Rust, dans le même src/
crate-type = ["cdylib"]
```

Concrètement, `src/` contient deux arborescences côte à côte :
`src/matrix/` (le paquet Python : `__init__.py`, `_core.pyi`, et le `.so`
compilé qui y atterrit automatiquement) et `src/rust/` (tout le code Rust :
`lib.rs`, `utils.rs`, `vector/`, `matrix/`). Le dossier Rust `matrix/`
porte le même nom que le paquet Python par coïncidence de vocabulaire (les
deux se réfèrent à la classe `Matrix`), mais ce sont deux dossiers
distincts, à des niveaux différents — Python n'a jamais besoin d'ouvrir
`src/rust/`, et Cargo (via le `path` ci-dessus) n'a jamais besoin d'ouvrir
`src/matrix/`. Un `uv sync` recompile automatiquement l'extension si le
Rust a changé, et place le `.so` directement dans `src/matrix/` à côté du
code Python :

```python
# src/matrix/__init__.py
from matrix._core import Matrix, Vector
```

## 9. Ce qu'il faut garder en tête

- **mypy ne voit pas dans le `.so`.** Un module compilé n'a pas de
  signatures Python inspectables ; il faut un fichier de stubs
  (`src/matrix/_core.pyi`) pour que mypy type-checke correctement le code
  qui l'utilise.
- **Chaque cycle "modifier le Rust → tester" repasse par une compilation.**
  Sur un projet de cette taille c'est de l'ordre de la seconde, mais ça
  reste un aller-retour de plus que Python pur.
- **Le typage Rust est plus strict.** Pas de conversion implicite
  int→float, pas d'indices négatifs gratuits, obligation de gérer
  explicitement les erreurs via `PyResult` : c'est le prix de la
  performance et de la sûreté mémoire, à payer même sur du code aussi
  simple qu'un `__getitem__`.

## 10. Pour aller plus loin

- Guide officiel PyO3 : <https://pyo3.rs>
- Guide officiel maturin : <https://www.maturin.rs>
- Le code de ce projet est le meilleur second exemple à lire dans l'ordre :
  `src/rust/vector/core/new.rs` → `len.rs` → `getitem.rs` → `iterator.rs` →
  `eq.rs` → `repr.rs` → `copy.rs`, puis la même chose côté `src/rust/matrix/`.
