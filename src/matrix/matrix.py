import math
from collections.abc import Iterable


class Matrix:
    """A matrix, stored row-major as a list of rows."""

    __slots__ = ("data",)

    def __init__(self, rows: Iterable[Iterable[float]]) -> None:
        self.data: list[list[float]] = [list(row) for row in rows]
        widths = {len(row) for row in self.data}
        if len(widths) > 1:
            raise ValueError("all rows of a matrix must have the same length")

    def copy(self) -> "Matrix":
        return Matrix(self.data)

    def shape(self) -> tuple[int, int]:
        """Return (rows, columns)."""
        rows = len(self.data)
        cols = len(self.data[0]) if rows else 0
        return rows, cols

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Matrix)
            and self.shape() == other.shape()
            and all(
                math.isclose(a, b, abs_tol=1e-9)
                for row_a, row_b in zip(self.data, other.data)
                for a, b in zip(row_a, row_b)
            )
        )

    def __repr__(self) -> str:
        rows = (
            "[" + ", ".join(str(x) for x in row) + "]" for row in self.data
        )
        return "\n" + "\n".join(rows)
