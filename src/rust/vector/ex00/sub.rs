use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    /// Subtract two vectors coordinate-wise and return a new vector.
    fn __sub__(&self, other: &Vector) -> PyResult<Vector> {
        self.zip_op(other, "cannot subtract vectors of different lengths", |a, b| {
            a - b
        })
    }
}
