use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn norm_1(&self) -> f64 {
        self.data
            .iter()
            .fold(0.0, |acc, &v| acc + if v < 0.0 { -v } else { v })
    }
}
