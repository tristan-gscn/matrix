import math

from matrix._core import Matrix


def projection(
    fov: float,
    ratio: float,
    near: float,
    far: float,
    *,
    radians: bool = False,
    column_major: bool = True,
) -> Matrix:
    if near <= 0:
        raise ValueError(f"near plane must be positive, got {near}")
    if far <= near:
        raise ValueError(
            f"far plane ({far}) must be strictly greater than "
            f"near plane ({near})"
        )
    if ratio <= 0:
        raise ValueError(f"aspect ratio must be positive, got {ratio}")

    fov_rad = fov if radians else math.radians(fov)
    if fov_rad <= 0 or fov_rad >= math.pi:
        raise ValueError(
            f"fov must be in range (0, 180) degrees or (0, pi) radians, "
            f"got {fov}"
        )

    sy = 1.0 / math.tan(fov_rad / 2.0)
    c = -far / (far - near)
    d = -(far * near) / (far - near)
    m = Matrix([
        [sy / ratio, 0.0, 0.0, 0.0],
        [0.0, sy, 0.0, 0.0],
        [0.0, 0.0, c, d],
        [0.0, 0.0, -1.0, 0.0],
    ])
    return m.transpose() if column_major else m
