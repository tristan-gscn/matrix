use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    /// Add two matrices element-wise and return a new matrix.
    fn __add__(&self, other: &Matrix) -> PyResult<Matrix> {
        self.zip_op(other, "cannot add matrices of different shapes", |a, b| {
            a + b
        })
    }
}