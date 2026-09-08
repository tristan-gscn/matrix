use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn __mul__(&self, a: f64) -> Vector {
        let data = self.data.iter().map(|&x| x * a).collect();
        Vector { data }
    }
}
