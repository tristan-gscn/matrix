import pytest
from matrix import Vector


class TestVectorMul:
    def test_basic_scaling(self) -> None:
        u = Vector([2.0, 3.0])
        result = u * 2.0
        assert result == Vector([4.0, 6.0])

    def test_scaling_by_int(self) -> None:
        u = Vector([2.0, 3.0])
        result = u * 2
        assert result == Vector([4.0, 6.0])

    def test_scale_by_zero(self) -> None:
        u = Vector([2.0, -3.5, 42.0])
        assert u * 0.0 == Vector([0.0, 0.0, 0.0])

    def test_scale_by_one(self) -> None:
        u = Vector([2.0, -3.5, 42.0])
        assert u * 1.0 == Vector([2.0, -3.5, 42.0])

    def test_scale_by_negative(self) -> None:
        u = Vector([2.0, -3.0])
        assert u * -1.5 == Vector([-3.0, 4.5])

    def test_empty_vector(self) -> None:
        u = Vector([])
        assert u * 2.0 == Vector([])

    def test_immutability(self) -> None:
        u = Vector([2.0, 3.0])
        _ = u * 2.0
        assert u == Vector([2.0, 3.0])

    def test_invalid_type_raises_type_error(self) -> None:
        u = Vector([1.0, 2.0])
        with pytest.raises(TypeError):
            _ = u * "scalar"  # type: ignore[operator]
        with pytest.raises(TypeError):
            _ = u * [1.0, 2.0]  # type: ignore[operator]
        with pytest.raises(TypeError):
            _ = u * u  # type: ignore[operator]
