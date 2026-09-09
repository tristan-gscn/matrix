import pytest
from matrix import Vector


class TestVectorNorm:
    def test_subject_example_zeros(self) -> None:
        u = Vector([0.0, 0.0, 0.0])
        assert u.norm() == 0.0

    def test_subject_example_positive(self) -> None:
        u = Vector([1.0, 2.0, 3.0])
        assert u.norm() == pytest.approx(3.74165738, abs=1e-6)

    def test_subject_example_negative(self) -> None:
        u = Vector([-1.0, -2.0])
        assert u.norm() == pytest.approx(2.236067977, abs=1e-6)

    def test_pythagorean_3_4_5(self) -> None:
        u = Vector([3.0, 4.0])
        assert u.norm() == pytest.approx(5.0)

    def test_negative_zero(self) -> None:
        u = Vector([-0.0, 0.0])
        assert u.norm() == 0.0

    def test_empty_vector(self) -> None:
        u = Vector([])
        assert u.norm() == 0.0

    def test_immutability(self) -> None:
        u = Vector([3.0, 4.0])
        _ = u.norm()
        assert u == Vector([3.0, 4.0])
