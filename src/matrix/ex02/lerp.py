from typing import TypeVar

from matrix._core import Matrix, Vector

T = TypeVar("T", float, Vector, Matrix)


def lerp(u: T, v: T, t: float) -> T:
    if type(u) is not type(v):
        raise TypeError("u and v must be of the same type")
    return u + (v - u) * t
