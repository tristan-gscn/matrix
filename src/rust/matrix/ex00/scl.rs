use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    /// Scale every element of this matrix by `a`, in place.
    fn scl(&mut self, a: f64) {
        todo!()
    }
}
