from collections.abc import Iterable

from .vector import Vector


class Matrix:
    """A matrix, stored row-major as a list of rows."""

    __slots__ = ("data",)

    def __init__(self, rows: Iterable[Iterable[float]]) -> None:
        self.data: list[list[float]] = [list(row) for row in rows]
        widths = {len(row) for row in self.data}
        if len(widths) > 1:
            raise ValueError("all rows of a matrix must have the same length")

    @classmethod
    def from_rows(cls, rows: Iterable[Iterable[float]]) -> "Matrix":
        return cls(rows)

    @classmethod
    def identity(cls, n: int) -> "Matrix":
        return cls(
            [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        )

    def copy(self) -> "Matrix":
        return Matrix(self.data)

    def shape(self) -> tuple[int, int]:
        """Return (rows, columns)."""
        rows = len(self.data)
        cols = len(self.data[0]) if rows else 0
        return rows, cols

    def is_square(self) -> bool:
        rows, cols = self.shape()
        return rows == cols

    def to_vector(self) -> Vector:
        """Flatten this matrix (row-major) into a vector."""
        return Vector([x for row in self.data for x in row])

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Matrix) and self.data == other.data

    def __repr__(self) -> str:
        rows = (
            "[" + ", ".join(str(x) for x in row) + "]" for row in self.data
        )
        return "\n" + "\n".join(rows)
