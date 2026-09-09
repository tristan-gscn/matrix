use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn norm_inf(&self) -> f64 {
        self.data
            .iter()
            .map(|&v| if v < 0.0 { -v } else { v })
            .fold(0.0, |max_val, v| max_val.max(v))
    }
}
