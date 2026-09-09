from matrix._core import Vector


def cross_product(u: Vector, v: Vector) -> Vector:
    if len(u) != 3 or len(v) != 3:
        raise ValueError(
            "cross product is only defined for 3-dimensional vectors"
        )
    return Vector([
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    ])
