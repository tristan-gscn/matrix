use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    pub(crate) fn __eq__(&self, other: &Matrix) -> bool {
        self.shape() == other.shape()
            && self
                .data
                .iter()
                .zip(&other.data)
                .all(|(ra, rb)| ra.iter().zip(rb).all(|(a, b)| (a - b).abs() < 1e-9))
    }
}
