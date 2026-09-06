use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    #[new]
    fn new(rows: Vec<Vec<f64>>) -> PyResult<Self> {
        if let Some(first) = rows.first() {
            if rows.iter().any(|row| row.len() != first.len()) {
                return Err(PyValueError::new_err(
                    "all rows of a matrix must have the same length",
                ));
            }
        }
        Ok(Matrix { data: rows })
    }
}
