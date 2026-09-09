use pyo3::exceptions::PyTypeError;
use pyo3::prelude::*;

use crate::matrix::Matrix;
use crate::vector::Vector;

#[pymethods]
impl Matrix {
    fn __mul__<'py>(&self, py: Python<'py>, other: &Bound<'py, PyAny>) -> PyResult<PyObject> {
        if let Ok(a) = other.extract::<f64>() {
            let data = self
                .data
                .iter()
                .map(|row| row.iter().map(|&x| x * a).collect())
                .collect();
            Ok(Matrix { data }.into_py(py))
        } else if let Ok(vec) = other.extract::<PyRef<Vector>>() {
            let res = self.mul_vec(&vec)?;
            Ok(res.into_py(py))
        } else if let Ok(mat) = other.extract::<PyRef<Matrix>>() {
            let res = self.mul_mat(&mat)?;
            Ok(res.into_py(py))
        } else {
            Err(PyTypeError::new_err(format!(
                "unsupported operand type(s) for *: 'Matrix' and '{}'",
                other.get_type().name()?
            )))
        }
    }
}
