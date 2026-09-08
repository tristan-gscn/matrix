import pytest
from matrix import Matrix


class TestMatrixMul:
    def test_basic_scaling_square(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        result = m * 2.0
        assert result == Matrix([[2.0, 4.0], [6.0, 8.0]])

    def test_scaling_by_int(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        result = m * 2
        assert result == Matrix([[2.0, 4.0], [6.0, 8.0]])

    def test_rectangular_matrix_scaling(self) -> None:
        m = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        result = m * 0.5
        assert result == Matrix([[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]])

    def test_scale_by_zero(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        assert m * 0.0 == Matrix([[0.0, 0.0], [0.0, 0.0]])

    def test_scale_by_one(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        assert m * 1.0 == Matrix([[1.0, 2.0], [3.0, 4.0]])

    def test_scale_by_negative(self) -> None:
        m = Matrix([[1.0, -2.0], [-3.0, 4.0]])
        assert m * -2.0 == Matrix([[-2.0, 4.0], [6.0, -8.0]])

    def test_single_element_matrix(self) -> None:
        m = Matrix([[42.0]])
        assert m * 0.5 == Matrix([[21.0]])

    def test_immutability(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        _ = m * 2.0
        assert m == Matrix([[1.0, 2.0], [3.0, 4.0]])

    def test_invalid_type_raises_type_error(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        with pytest.raises(TypeError):
            _ = m * "scalar"  # type: ignore[operator]
        with pytest.raises(TypeError):
            _ = m * [1.0, 2.0]  # type: ignore[operator]
        with pytest.raises(TypeError):
            _ = m * m  # type: ignore[operator]
