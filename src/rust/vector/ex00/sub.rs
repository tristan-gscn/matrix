use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    /// Subtract two vectors coordinate-wise and return a new vector.
    fn __sub__(&self, other: &Vector) -> PyResult<Vector> {
        (self.data.len() == other.data.len())
            .then(|| {
                let data = self
                    .data
                    .iter()
                    .zip(&other.data)
                    .map(|(&a, &b)| a - b)
                    .collect();
                Vector { data }
            })
            .ok_or_else(|| {
                PyValueError::new_err(
                    "cannot subtract vectors of different lengths",
                )
            })
    }
}
