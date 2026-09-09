use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    pub fn determinant(&self) -> PyResult<f64> {
        let (rows, cols) = self.shape();
        if rows != cols {
            return Err(PyValueError::new_err(format!(
                "cannot compute determinant of non-square matrix of shape ({rows}, {cols})"
            )));
        }

        if rows == 0 {
            return Ok(1.0);
        }

        let (echelon, swaps, _) = self.row_echelon_form(false);
        let diagonal_product: f64 = echelon
            .data
            .iter()
            .enumerate()
            .map(|(i, row)| row[i])
            .product();
        let sign = if swaps % 2 == 0 { 1.0 } else { -1.0 };

        Ok(sign * diagonal_product)
    }
}
