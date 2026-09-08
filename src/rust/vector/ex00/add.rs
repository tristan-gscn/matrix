use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    /// Add two vectors coordinate-wise and return a new vector.
    fn __add__(&self, other: &Vector) -> PyResult<Vector> {
        self.zip_op(other, "cannot add vectors of different lengths", |a, b| {
            a + b
        })
    }
}
