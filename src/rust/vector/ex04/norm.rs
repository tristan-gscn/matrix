use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn norm(&self) -> f64 {
        self.data
            .iter()
            .map(|&v| v * v)
            .sum::<f64>()
            .powf(0.5)
    }
}
