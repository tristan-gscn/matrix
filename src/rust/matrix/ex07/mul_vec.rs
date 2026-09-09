use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::matrix::Matrix;
use crate::vector::Vector;

#[pymethods]
impl Matrix {
    pub fn mul_vec(&self, vec: &Vector) -> PyResult<Vector> {
        let (rows, cols) = self.shape();
        if cols != vec.data.len() {
            return Err(PyValueError::new_err(format!(
                "cannot multiply matrix of shape ({rows}, {cols}) with vector of length {}",
                vec.data.len()
            )));
        }

        let data = self
            .data
            .iter()
            .map(|row| {
                row.iter()
                    .zip(&vec.data)
                    .map(|(&m, &v)| m * v)
                    .sum::<f64>()
            })
            .collect();

        Ok(Vector { data })
    }
}
