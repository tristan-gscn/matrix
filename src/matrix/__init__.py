from .matrix import Matrix
from .vector import Vector

__all__ = ["Vector", "Matrix"]


def main() -> None:
    u = Vector([2.0, 3.0])
    m = Matrix([[1.0, 0.0], [0.0, 1.0]])
    print(f"Vector: {u}")
    print(f"Matrix: {m}")
