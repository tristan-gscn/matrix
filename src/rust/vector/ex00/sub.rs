use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    /// Subtract `v` from this vector, coordinate-wise, in place.
    fn sub(&mut self, _v: &Vector) -> PyResult<()> {
        todo!()
    }
}
