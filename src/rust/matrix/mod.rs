mod core;
mod ex00;
pub mod ex07;
pub mod ex08;
pub mod ex09;
pub mod ex10;
pub mod ex11;
pub mod ex12;
pub mod ex13;

use pyo3::prelude::*;

/// A matrix, stored row-major as a list of rows.
#[pyclass(subclass)]
pub struct Matrix {
    pub data: Vec<Vec<f64>>,
}
