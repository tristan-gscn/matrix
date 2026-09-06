use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    /// Return (rows, columns).
    pub fn shape(&self) -> (usize, usize) {
        let rows = self.data.len();
        let cols = self.data.first().map_or(0, |r| r.len());
        (rows, cols)
    }
}
