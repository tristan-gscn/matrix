use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    /// Subtract `v` from this matrix, element-wise, in place.
    fn sub(&mut self, _v: &Matrix) -> PyResult<()> {
        todo!()
    }
}
