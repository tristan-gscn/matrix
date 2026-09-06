use pyo3::prelude::*;

use crate::vector::{Vector, VectorIter};

#[pymethods]
impl Vector {
    fn __iter__(&self) -> VectorIter {
        VectorIter::new(self.data.clone())
    }
}
