use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn __add__(&self, other: &Vector) -> PyResult<Vector> {
        (self.data.len() == other.data.len())
            .then(|| {
                let data = self
                    .data
                    .iter()
                    .zip(&other.data)
                    .map(|(a, b)| a + b)
                    .collect();
                Vector { data }
            })
            .ok_or_else(|| PyValueError::new_err("cannot add vectors of different lengths"))
    }
}
