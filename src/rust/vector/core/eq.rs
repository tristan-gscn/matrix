use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn __eq__(&self, other: &Vector) -> bool {
        self.data.len() == other.data.len()
            && self
                .data
                .iter()
                .zip(&other.data)
                .all(|(a, b)| (a - b).abs() < 1e-9)
    }
}
