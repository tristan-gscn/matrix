use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    /// Build a copy by calling `type(self)(data)`, so a Python subclass of
    /// `Matrix` gets back an instance of itself rather than the base type.
    fn copy(slf: &Bound<'_, Self>) -> PyResult<PyObject> {
        let data = slf.borrow().data.clone();
        slf.get_type().call1((data,)).map(Bound::unbind)
    }
}
