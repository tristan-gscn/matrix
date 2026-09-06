use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    /// Scale every coordinate of this vector by `a`, in place.
    fn scl(&mut self, a: f64) {
        todo!()
    }
}
