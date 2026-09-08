use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    /// Subtract two matrices element-wise and return a new matrix.
    fn __sub__(&self, other: &Matrix) -> PyResult<Matrix> {
        self.zip_op(other, "cannot subtract matrices of different shapes", |a, b| {
            a - b
        })
    }
}
