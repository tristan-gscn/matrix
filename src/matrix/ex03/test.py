import pytest
from matrix import Vector


class TestVectorDot:
    def test_subject_example_orthogonal_zeros(self) -> None:
        u = Vector([0.0, 0.0])
        v = Vector([1.0, 1.0])
        assert u.dot(v) == 0.0

    def test_subject_example_ones(self) -> None:
        u = Vector([1.0, 1.0])
        v = Vector([1.0, 1.0])
        assert u.dot(v) == 2.0

    def test_subject_example_general(self) -> None:
        u = Vector([-1.0, 6.0])
        v = Vector([3.0, 2.0])
        assert u.dot(v) == 9.0

    def test_orthogonal_canonical(self) -> None:
        u = Vector([1.0, 0.0, 0.0])
        v = Vector([0.0, 1.0, 0.0])
        assert u.dot(v) == 0.0

    def test_commutativity(self) -> None:
        u = Vector([2.0, -3.5, 4.0])
        v = Vector([-1.0, 2.0, 0.5])
        assert u.dot(v) == pytest.approx(v.dot(u))

    def test_distributivity_over_addition(self) -> None:
        u = Vector([1.0, 2.0, 3.0])
        v = Vector([4.0, 5.0, 6.0])
        w = Vector([7.0, 8.0, 9.0])
        assert u.dot(v + w) == pytest.approx(u.dot(v) + u.dot(w))

    def test_scalar_homogeneity(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([3.0, 4.0])
        assert (u * 2.5).dot(v) == pytest.approx(2.5 * u.dot(v))

    def test_empty_vectors(self) -> None:
        u = Vector([])
        v = Vector([])
        assert u.dot(v) == 0.0

    def test_immutability(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([3.0, 4.0])
        _ = u.dot(v)
        assert u == Vector([1.0, 2.0])
        assert v == Vector([3.0, 4.0])

    def test_dimension_mismatch_raises_value_error(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([1.0, 2.0, 3.0])
        with pytest.raises(ValueError):
            _ = u.dot(v)

    def test_invalid_type_raises_type_error(self) -> None:
        u = Vector([1.0, 2.0])
        with pytest.raises(TypeError):
            _ = u.dot([1.0, 2.0])  # type: ignore[arg-type]
        with pytest.raises(TypeError):
            _ = u.dot(42)  # type: ignore[arg-type]
