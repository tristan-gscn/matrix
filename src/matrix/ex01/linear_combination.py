from collections.abc import Sequence
from matrix._core import Vector


def linear_combination(
    vectors: Sequence[Vector], coefs: Sequence[float]
) -> Vector:
    if len(vectors) != len(coefs):
        raise ValueError("number of vectors and coefficients must match")
    if not vectors:
        return Vector([])
    if len({len(v) for v in vectors}) != 1:
        raise ValueError("incoherent vector dimensions")

    return Vector([
        sum(c * v[i] for v, c in zip(vectors, coefs))
        for i in range(len(vectors[0]))
    ])
