use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    pub fn inverse(&self) -> PyResult<Matrix> {
        let (rows, cols) = self.shape();
        if rows != cols {
            return Err(PyValueError::new_err(format!(
                "cannot compute inverse of non-square matrix of shape ({rows}, {cols})"
            )));
        }

        if rows == 0 {
            return Ok(Matrix { data: vec![] });
        }

        let identity = Matrix::identity(rows);

        let augmented = self
            .data
            .iter()
            .zip(&identity.data)
            .map(|(row, id_row)| row.iter().chain(id_row).copied().collect())
            .collect();

        let (reduced, _, _) = Matrix { data: augmented }.row_echelon_form(true);

        Matrix {
            data: reduced.data.iter().map(|row| row[..rows].to_vec()).collect(),
        }
        .__eq__(&identity)
        .then_some(())
        .ok_or_else(|| PyValueError::new_err("matrix is singular and has no inverse"))?;

        let data = reduced
            .data
            .into_iter()
            .map(|row| row[rows..].to_vec())
            .collect();

        Ok(Matrix { data })
    }
}
