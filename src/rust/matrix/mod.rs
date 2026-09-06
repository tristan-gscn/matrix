mod core;

use pyo3::prelude::*;

/// A matrix, stored row-major as a list of rows.
#[pyclass(subclass)]
pub struct Matrix {
    pub data: Vec<Vec<f64>>,
}
