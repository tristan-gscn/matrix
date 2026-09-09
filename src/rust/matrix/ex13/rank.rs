use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    pub fn rank(&self) -> usize {
        self.row_echelon_form(false).2
    }
}
