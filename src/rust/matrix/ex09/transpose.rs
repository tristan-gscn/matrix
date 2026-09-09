use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    pub fn transpose(&self) -> Matrix {
        let (_, cols) = self.shape();
        let data = (0..cols)
            .map(|j| self.data.iter().map(|row| row[j]).collect())
            .collect();
        Matrix { data }
    }
}
