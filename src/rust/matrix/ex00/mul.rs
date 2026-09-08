use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    fn __mul__(&self, a: f64) -> Matrix {
        let data = self
            .data
            .iter()
            .map(|row| row.iter().map(|&x| x * a).collect())
            .collect();
        Matrix { data }
    }
}
