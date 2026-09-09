use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    /// Subtract two matrices element-wise and return a new matrix.
    fn __sub__(&self, other: &Matrix) -> PyResult<Matrix> {
        (self.shape() == other.shape())
            .then(|| {
                let data = self
                    .data
                    .iter()
                    .zip(&other.data)
                    .map(|(row_a, row_b)| {
                        row_a.iter().zip(row_b).map(|(&a, &b)| a - b).collect()
                    })
                    .collect();
                Matrix { data }
            })
            .ok_or_else(|| {
                PyValueError::new_err(
                    "cannot subtract matrices of different shapes",
                )
            })
    }
}
