use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn __repr__(&self) -> String {
        let rows: Vec<String> = self.data.iter().map(|x| format!("[{x:?}]")).collect();
        format!("\n{}", rows.join("\n"))
    }
}
