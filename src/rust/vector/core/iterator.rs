use pyo3::prelude::*;

/// Iterator over a `Vector`'s coordinates, in order.
#[pyclass]
pub struct VectorIter {
    data: Vec<f64>,
    index: usize,
}

impl VectorIter {
    pub fn new(data: Vec<f64>) -> Self {
        VectorIter { data, index: 0 }
    }
}

#[pymethods]
impl VectorIter {
    fn __iter__(slf: PyRef<'_, Self>) -> PyRef<'_, Self> {
        slf
    }

    fn __next__(&mut self) -> Option<f64> {
        let item = self.data.get(self.index).copied();
        self.index += 1;
        item
    }
}
