use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    /// Add `v` into this vector, coordinate-wise, in place.
    fn add(&mut self, v: &Vector) -> PyResult<()> {
        todo!()
    }
}
