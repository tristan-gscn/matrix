use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    #[staticmethod]
    pub fn identity(n: usize) -> Matrix {
        Matrix {
            data: (0..n)
                .map(|i| (0..n).map(|j| if i == j { 1.0 } else { 0.0 }).collect())
                .collect(),
        }
    }
}
