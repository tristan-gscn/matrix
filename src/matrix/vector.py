import math
from collections.abc import Iterable, Iterator


class Vector:
    """A finite-dimensional vector, stored as a flat list of coordinates."""

    __slots__ = ("data",)

    def __init__(self, data: Iterable[float]) -> None:
        self.data: list[float] = list(data)

    def copy(self) -> "Vector":
        return Vector(self.data)

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator[float]:
        return iter(self.data)

    def __getitem__(self, index: int) -> float:
        return self.data[index]

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Vector)
            and len(self.data) == len(other.data)
            and all(
                math.isclose(a, b, abs_tol=1e-9)
                for a, b in zip(self.data, other.data)
            )
        )

    def __repr__(self) -> str:
        return "\n" + "\n".join(f"[{x}]" for x in self.data)
