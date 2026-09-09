mod core;
mod ex00;
mod ex03;

pub use core::VectorIter;

use pyo3::prelude::*;

/// A finite-dimensional vector, stored as a flat list of coordinates.
#[pyclass(subclass)]
pub struct Vector {
    pub data: Vec<f64>,
}
