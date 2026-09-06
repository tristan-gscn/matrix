use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    fn __repr__(&self) -> String {
        let rows: Vec<String> = self
            .data
            .iter()
            .map(|row| {
                let items: Vec<String> = row.iter().map(|x| format!("{x:?}")).collect();
                format!("[{}]", items.join(", "))
            })
            .collect();
        format!("\n{}", rows.join("\n"))
    }
}
