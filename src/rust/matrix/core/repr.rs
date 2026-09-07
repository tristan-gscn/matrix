use pyo3::prelude::*;

use crate::matrix::Matrix;

#[pymethods]
impl Matrix {
    fn __repr__(&self) -> String {
        let cols = self.data.first().map_or(0, |row| row.len());
        let cells: Vec<Vec<String>> = self
            .data
            .iter()
            .map(|row| row.iter().map(|x| format!("{x:?}")).collect())
            .collect();

        let mut widths = vec![0usize; cols];
        for row in &cells {
            for (w, cell) in widths.iter_mut().zip(row) {
                *w = (*w).max(cell.chars().count());
            }
        }

        let lines: Vec<String> = cells
            .iter()
            .map(|row| {
                let padded: Vec<String> = row
                    .iter()
                    .zip(&widths)
                    .map(|(cell, &w)| format!("{cell:>w$}"))
                    .collect();
                format!("│ {} │", padded.join("  "))
            })
            .collect();

        let inner_width = lines.first().map_or(2, |l| l.chars().count() - 2);
        let top = format!("┌{}┐", " ".repeat(inner_width));
        let bottom = format!("└{}┘", " ".repeat(inner_width));
        format!("\n{top}\n{}\n{bottom}", lines.join("\n"))
    }
}
