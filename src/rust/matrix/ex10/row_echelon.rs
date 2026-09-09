use pyo3::prelude::*;

use crate::matrix::Matrix;

const EPSILON: f64 = 1e-9;

#[pymethods]
impl Matrix {
    pub fn row_echelon(&self) -> Matrix {
        let (rows, cols) = self.shape();
        if rows == 0 || cols == 0 {
            return Matrix {
                data: self.data.clone(),
            };
        }

        let mut data = self.data.clone();
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

            data.swap(pivot_row, best_row);
            let pivot_val = data[pivot_row][col];
            let pivot_line: Vec<f64> = data[pivot_row].iter().map(|&x| x / pivot_val).collect();

            data = data
                .into_iter()
                .enumerate()
                .map(|(r, row)| {
                    if r == pivot_row {
                        pivot_line.clone()
                    } else {
                        let factor = row[col];
                        row.iter()
                            .zip(&pivot_line)
                            .map(|(&x, &p)| x - factor * p)
                            .collect()
                    }
                })
                .collect();

            pivot_row += 1;
        }

        // 4. Nettoyer les résidus flottants et -0.0
        let data = data
            .into_iter()
            .map(|row| {
                row.into_iter()
                    .map(|x| if x.abs() < EPSILON { 0.0 } else { x })
                    .collect()
            })
            .collect();

        Matrix { data }
    }
}
