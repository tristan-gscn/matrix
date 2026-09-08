import pytest
from matrix import Matrix, Vector


class TestMatrixAdd:
    def test_basic_addition_square(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        result = m1 + m2
        assert result == Matrix([[8.0, 6.0], [1.0, 6.0]])

    def test_rectangular_matrix_addition(self) -> None:
        m1 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        m2 = Matrix([[10.0, 20.0, 30.0], [40.0, 50.0, 60.0]])
        result = m1 + m2
        assert result == Matrix([[11.0, 22.0, 33.0], [44.0, 55.0, 66.0]])

    def test_negative_and_zero_values(self) -> None:
        m1 = Matrix([[1.0, -3.0], [0.0, 5.0]])
        m2 = Matrix([[-1.0, 3.0], [0.0, -5.0]])
        result = m1 + m2
        assert result == Matrix([[0.0, 0.0], [0.0, 0.0]])

    def test_single_element_matrix(self) -> None:
        m1 = Matrix([[5.0]])
        m2 = Matrix([[-2.0]])
        assert m1 + m2 == Matrix([[3.0]])

    def test_commutativity(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[5.0, 6.0], [7.0, 8.0]])
        assert m1 + m2 == m2 + m1

    def test_associativity(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[5.0, 6.0], [7.0, 8.0]])
        m3 = Matrix([[9.0, 10.0], [11.0, 12.0]])
        assert (m1 + m2) + m3 == m1 + (m2 + m3)

    def test_immutability(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[5.0, 6.0], [7.0, 8.0]])
        _ = m1 + m2
        assert m1 == Matrix([[1.0, 2.0], [3.0, 4.0]])
        assert m2 == Matrix([[5.0, 6.0], [7.0, 8.0]])

    def test_shape_mismatch_different_rows(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[1.0, 2.0]])
        err_msg = "cannot add matrices of different shapes"
        with pytest.raises(ValueError, match=err_msg):
            _ = m1 + m2

    def test_shape_mismatch_different_cols(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        err_msg = "cannot add matrices of different shapes"
        with pytest.raises(ValueError, match=err_msg):
            _ = m1 + m2

    def test_shape_mismatch_transposed_dimensions(self) -> None:
        m1 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  # 2x3
        m2 = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])  # 3x2
        err_msg = "cannot add matrices of different shapes"
        with pytest.raises(ValueError, match=err_msg):
            _ = m1 + m2

    def test_invalid_type_raises_type_error(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Vector([1.0, 2.0])
        with pytest.raises(TypeError):
            _ = m + 42  # type: ignore[operator]
        with pytest.raises(TypeError):
            _ = m + v  # type: ignore[operator]
