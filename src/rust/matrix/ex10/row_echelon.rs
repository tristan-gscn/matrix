use pyo3::prelude::*;

use crate::matrix::Matrix;

const EPSILON: f64 = 1e-9;

impl Matrix {
    pub(crate) fn row_echelon_form(&self, reduce: bool) -> (Matrix, u32, usize) {
        let (rows, cols) = self.shape();
        if rows == 0 || cols == 0 {
            return (
                Matrix {
                    data: self.data.clone(),
                },
                0,
                0,
            );
        }

        let mut data = self.data.clone();
        let mut swaps = 0;
        let mut pivot_row = 0;

        for col in 0..cols {
            if pivot_row >= rows {
                break;
            }

            let best_row = (pivot_row..rows).max_by(|&a, &b| {
                data[a][col]
                    .abs()
                    .total_cmp(&data[b][col].abs())
            });
            let Some(best_row) = best_row else { continue };
            if data[best_row][col].abs() < EPSILON {
                continue;
            }

            if best_row != pivot_row {
                data.swap(pivot_row, best_row);
                swaps += 1;
            }

            let pivot_val = data[pivot_row][col];
            let pivot_line: Vec<f64> = if reduce {
                data[pivot_row].iter().map(|&x| x / pivot_val).collect()
            } else {
                data[pivot_row].clone()
            };

            data = data
                .into_iter()
                .enumerate()
                .map(|(r, row)| {
                    if r == pivot_row {
                        pivot_line.clone()
                    } else if !reduce && r < pivot_row {
                        row
                    } else {
                        let factor = if reduce { row[col] } else { row[col] / pivot_val };
                        row.iter()
                            .zip(&pivot_line)
                            .map(|(&x, &p)| x - factor * p)
                            .collect()
                    }
                })
                .collect();

            pivot_row += 1;
        }

        let data = data
            .into_iter()
            .map(|row| {
                row.into_iter()
                    .map(|x| if x.abs() < EPSILON { 0.0 } else { x })
                    .collect()
            })
            .collect();

        (Matrix { data }, swaps, pivot_row)
    }
}

#[pymethods]
impl Matrix {
    #[pyo3(signature = (reduce = true))]
    pub fn row_echelon(&self, reduce: bool) -> Matrix {
        self.row_echelon_form(reduce).0
    }
}
