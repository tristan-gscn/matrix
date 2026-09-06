use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    /// Build a copy by calling `type(self)(data)`, so a Python subclass of
    /// `Vector` gets back an instance of itself rather than the base type.
    fn copy(slf: &Bound<'_, Self>) -> PyResult<PyObject> {
        let data = slf.borrow().data.clone();
        slf.get_type().call1((data,)).map(Bound::unbind)
    }
}
