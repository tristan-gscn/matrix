use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    pub fn trace(&self) -> PyResult<f64> {
        let (rows, cols) = self.shape();
        if rows != cols {
            return Err(PyValueError::new_err(format!(
                "cannot compute trace of non-square matrix of shape ({rows}, {cols})"
            )));
        }

        if cols == 0 {
            return Ok(0.0);
        }

        Ok(self
            .data
            .iter()
            .flatten()
            .copied()
            .step_by(cols + 1)
            .fold(0.0, |acc, x| acc + x)
        )
    }
}