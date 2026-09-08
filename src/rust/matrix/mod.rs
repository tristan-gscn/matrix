mod core;
mod ex00;

use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

/// A matrix, stored row-major as a list of rows.
#[pyclass(subclass)]
pub struct Matrix {
    pub data: Vec<Vec<f64>>,
}

impl Matrix {
    pub(crate) fn zip_op(
        &self,
        other: &Matrix,
        err_msg: &'static str,
        op: impl Fn(f64, f64) -> f64,
    ) -> PyResult<Matrix> {
        (self.shape() == other.shape())
            .then(|| {
                let data = self
                    .data
                    .iter()
                    .zip(&other.data)
                    .map(|(row_a, row_b)| {
                        row_a.iter().zip(row_b).map(|(&a, &b)| op(a, b)).collect()
                    })
                    .collect();
                Matrix { data }
            })
            .ok_or_else(|| PyValueError::new_err(err_msg))
    }
}
