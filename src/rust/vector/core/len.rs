use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn __len__(&self) -> usize {
        self.data.len()
    }
}
