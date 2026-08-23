from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .matrix import Matrix


class Vector:
    """A finite-dimensional vector, stored as a flat list of coordinates."""

    __slots__ = ("data",)

    def __init__(self, data: Iterable[float]) -> None:
        self.data: list[float] = list(data)

    @classmethod
    def from_list(cls, data: Iterable[float]) -> "Vector":
        return cls(data)

    def copy(self) -> "Vector":
        return Vector(self.data)

    def size(self) -> int:
        """Return the dimension of the vector."""
        return len(self.data)

    def to_matrix(self, rows: int, cols: int) -> "Matrix":
        """Reshape this vector into a `rows`-by-`cols` matrix (row-major)."""
        from .matrix import Matrix

        if rows * cols != self.size():
            raise ValueError(
                f"cannot reshape a vector of size {self.size()} into a "
                f"{rows}x{cols} matrix"
            )
        return Matrix(
            [self.data[i * cols:(i + 1) * cols] for i in range(rows)]
        )

    def __len__(self) -> int:
        return self.size()

    def __iter__(self) -> Iterator[float]:
        return iter(self.data)

    def __getitem__(self, index: int) -> float:
        return self.data[index]

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and self.data == other.data

    def __repr__(self) -> str:
        return "\n" + "\n".join(f"[{x}]" for x in self.data)
