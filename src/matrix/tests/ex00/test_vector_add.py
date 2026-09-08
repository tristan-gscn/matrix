import pytest
from matrix import Vector


class TestVectorAdd:
    def test_basic_addition(self) -> None:
        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        result = u + v
        assert result == Vector([7.0, 10.0])

    def test_negative_and_zero_values(self) -> None:
        u = Vector([1.0, -2.5, 0.0])
        v = Vector([-1.0, 2.5, 0.0])
        result = u + v
        assert result == Vector([0.0, 0.0, 0.0])

    def test_empty_vectors(self) -> None:
        u = Vector([])
        v = Vector([])
        result = u + v
        assert result == Vector([])

    def test_single_element(self) -> None:
        u = Vector([42.0])
        v = Vector([-10.0])
        assert u + v == Vector([32.0])

    def test_commutativity(self) -> None:
        u = Vector([1.5, 2.5, 3.5])
        v = Vector([4.0, 5.0, 6.0])
        assert u + v == v + u

    def test_associativity(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([3.0, 4.0])
        w = Vector([5.0, 6.0])
        assert (u + v) + w == u + (v + w)

    def test_immutability(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([3.0, 4.0])
        _ = u + v
        assert u == Vector([1.0, 2.0])
        assert v == Vector([3.0, 4.0])

    def test_dimension_mismatch_raises_value_error(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([1.0, 2.0, 3.0])
        err_msg = "cannot add vectors of different lengths"
        with pytest.raises(ValueError, match=err_msg):
            _ = u + v

    def test_empty_and_non_empty_mismatch(self) -> None:
        u = Vector([])
        v = Vector([1.0])
        err_msg = "cannot add vectors of different lengths"
        with pytest.raises(ValueError, match=err_msg):
            _ = u + v

    def test_invalid_type_raises_type_error(self) -> None:
        u = Vector([1.0, 2.0])
        with pytest.raises(TypeError):
            _ = u + 42  # type: ignore[operator]
        with pytest.raises(TypeError):
            _ = u + [1.0, 2.0]  # type: ignore[operator]
