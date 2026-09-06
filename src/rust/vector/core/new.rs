use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    #[new]
    fn new(data: Vec<f64>) -> Self {
        Vector { data }
    }
}
