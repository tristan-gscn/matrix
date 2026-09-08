mod core;
mod ex00;

pub use core::VectorIter;

use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

/// A finite-dimensional vector, stored as a flat list of coordinates.
#[pyclass(subclass)]
pub struct Vector {
    pub data: Vec<f64>,
}

impl Vector {
    pub(crate) fn zip_op(
        &self,
        other: &Vector,
        err_msg: &'static str,
        op: impl Fn(f64, f64) -> f64,
    ) -> PyResult<Vector> {
        (self.data.len() == other.data.len())
            .then(|| {
                let data = self
                    .data
                    .iter()
                    .zip(&other.data)
                    .map(|(&a, &b)| op(a, b))
                    .collect();
                Vector { data }
            })
            .ok_or_else(|| PyValueError::new_err(err_msg))
    }
}
