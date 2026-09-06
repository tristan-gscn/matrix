use pyo3::exceptions::PyIndexError;
use pyo3::prelude::*;

use crate::utils::normalize_index;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn __getitem__(&self, index: isize) -> PyResult<f64> {
        normalize_index(index, self.data.len())
            .map(|i| self.data[i])
            .ok_or_else(|| PyIndexError::new_err("vector index out of range"))
    }
}
