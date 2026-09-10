*This project has been created as part of the 42 curriculum by trgascoi.*

# Matrix

A linear algebra library implementing fundamental vector and matrix operations from scratch, built with high-performance **Rust** computational kernels bound to **Python** via **PyO3**.

### Exercises

| Exercise | Topic | Description |
| :--- | :--- | :--- |
| **ex00** | Add, Subtract & Scale | Elementary vector and matrix arithmetic (`+`, `-`, `*`) |
| **ex01** | Linear combination | Computes linear combinations of vector sequences |
| **ex02** | Linear interpolation | Generic linear interpolation (`lerp`) for scalars, vectors, and matrices |
| **ex03** | Dot product | Inner product between two vectors |
| **ex04** | Norm | Manhattan (L1), Euclidean (L2), and Chebyshev (L-inf) norms |
| **ex05** | Cosine | Cosine of the angle between two vectors |
| **ex06** | Cross product | 3D vector cross product (u x v) |
| **ex07** | Matrix multiplication | Matrix-vector and matrix-matrix multiplications |
| **ex08** | Trace | Sum of diagonal elements of a square matrix |
| **ex09** | Transpose | Row-column reflection of a matrix |
| **ex10** | Row-echelon form | Gaussian elimination with partial pivoting (REF / RREF) |
| **ex11** | Determinant | Matrix determinant computed via Gaussian reduction |
| **ex12** | Inverse | Matrix inverse via Gauss-Jordan elimination on [A \| I] |
| **ex13** | Rank | Matrix rank (number of independent pivot rows) |
| **ex14** | Projection matrix *(Bonus)* | 3D perspective projection matrix integrated with 42 `display` visualizer |

## Instructions

### Build

Compile the Rust core and install the Python bindings:

```bash
make
```

### Execution

Run the demo for any specific exercise:

```bash
make run ARGS=00    # Run exercise 00
make run ARGS=14    # Run exercise 14
```

### 3D Projection Display (Bonus)

Generate the projection matrix and launch the interactive 3D visualizer:

```bash
make display
# or with custom parameters:
make display ARGS="60 1.7777 1.0 50"
```

*Controls:* `W/A/S/D` to move, Mouse to look around, `Esc` to quit.

### Tests & Quality

```bash
make test           # Run all 227 unit tests (pytest)
make lint           # Check typing (mypy) and PEP8 formatting (flake8)
make clean          # Remove build artifacts
```
