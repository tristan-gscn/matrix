use pyo3::prelude::*;

use crate::vector::Vector;

#[pymethods]
impl Vector {
    fn __repr__(&self) -> String {
        let cells: Vec<String> = self.data.iter().map(|x| format!("{x:?}")).collect();
        let width = cells.iter().map(|c| c.chars().count()).max().unwrap_or(0);
        let lines: Vec<String> = cells
            .iter()
            .map(|c| format!("│ {c:>width$} │"))
            .collect();
        let inner_width = lines.first().map_or(2, |l| l.chars().count() - 2);
        let top = format!("┌{}┐", " ".repeat(inner_width));
        let bottom = format!("└{}┘", " ".repeat(inner_width));
        format!("\n{top}\n{}\n{bottom}", lines.join("\n"))
    }
}
