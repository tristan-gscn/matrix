use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    /// Add `v` into this matrix, element-wise, in place.
    fn add(&mut self, v: &Matrix) -> PyResult<()> {
        todo!()
    }
}
