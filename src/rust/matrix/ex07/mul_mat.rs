use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    pub fn mul_mat(&self, mat: &Matrix) -> PyResult<Matrix> {
        let (m, n) = self.shape();
        let (p, q) = mat.shape();
        if n != p {
            return Err(PyValueError::new_err(format!(
                "cannot multiply matrix of shape ({m}, {n}) with matrix of shape ({p}, {q})"
            )));
        }

        let cols: Vec<Vec<f64>> = (0..q)
            .map(|j| mat.data.iter().map(|row| row[j]).collect())
            .collect();

        let data = self
            .data
            .iter()
            .map(|row| {
                cols.iter()
                    .map(|col| {
                        row.iter()
                            .zip(col)
                            .map(|(&a, &b)| a * b)
                            .sum::<f64>()
                    })
                    .collect()
            })
            .collect();

        Ok(Matrix { data })
    }
}
