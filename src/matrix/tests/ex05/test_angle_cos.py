import pytest
from matrix import Vector, angle_cos


class TestAngleCos:
    def test_subject_example_same_direction(self) -> None:
        u = Vector([1.0, 0.0])
        v = Vector([1.0, 0.0])
        assert angle_cos(u, v) == pytest.approx(1.0)

    def test_subject_example_orthogonal(self) -> None:
        u = Vector([1.0, 0.0])
        v = Vector([0.0, 1.0])
        assert angle_cos(u, v) == pytest.approx(0.0)

    def test_subject_example_opposite_direction(self) -> None:
        u = Vector([-1.0, 1.0])
        v = Vector([1.0, -1.0])
        assert angle_cos(u, v) == pytest.approx(-1.0)

    def test_subject_example_collinear_scaled(self) -> None:
        u = Vector([2.0, 1.0])
        v = Vector([4.0, 2.0])
        assert angle_cos(u, v) == pytest.approx(1.0)

    def test_subject_example_3d(self) -> None:
        u = Vector([1.0, 2.0, 3.0])
        v = Vector([4.0, 5.0, 6.0])
        assert angle_cos(u, v) == pytest.approx(0.974631846, abs=1e-6)

    def test_symmetry(self) -> None:
        u = Vector([1.0, 2.0, 3.0])
        v = Vector([4.0, 5.0, 6.0])
        assert angle_cos(u, v) == pytest.approx(angle_cos(v, u))

    def test_scale_invariance(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([3.0, 4.0])
        base_cos = angle_cos(u, v)
        assert angle_cos(u * 4.2, v * 0.5) == pytest.approx(base_cos)

    def test_immutability(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([3.0, 4.0])
        _ = angle_cos(u, v)
        assert u == Vector([1.0, 2.0])
        assert v == Vector([3.0, 4.0])

    def test_dimension_mismatch_raises_value_error(self) -> None:
        u = Vector([1.0, 0.0])
        v = Vector([1.0, 0.0, 0.0])
        with pytest.raises(ValueError):
            _ = angle_cos(u, v)

    def test_zero_vector_raises_zero_division_error(self) -> None:
        zero = Vector([0.0, 0.0])
        v = Vector([1.0, 2.0])
        with pytest.raises(ZeroDivisionError):
            _ = angle_cos(zero, v)
        with pytest.raises(ZeroDivisionError):
            _ = angle_cos(v, zero)
        with pytest.raises(ZeroDivisionError):
            _ = angle_cos(zero, zero)
