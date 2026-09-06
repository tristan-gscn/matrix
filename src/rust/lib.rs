mod matrix;
mod utils;
mod vector;

use pyo3::prelude::*;

use matrix::Matrix;
use vector::{Vector, VectorIter};

#[pymodule]
fn _core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Vector>()?;
    m.add_class::<VectorIter>()?;
    m.add_class::<Matrix>()?;
    Ok(())
}
