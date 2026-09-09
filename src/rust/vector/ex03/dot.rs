use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn dot(&self, other: &Vector) -> PyResult<f64> {
        (self.data.len() == other.data.len())
            .then(|| {
                self.data
                    .iter()
                    .zip(&other.data)
                    .map(|(&a, &b)| a * b)
                    .sum()
            })
            .ok_or_else(|| {
                PyValueError::new_err(
                    "cannot compute dot product of vectors of different lengths",
                )
            })
    }
}