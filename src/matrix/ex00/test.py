import pytest
from matrix import Matrix, Vector


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


class TestVectorSub:
    def test_basic_subtraction(self) -> None:
        u = Vector([2.0, 3.0])
        v = Vector([5.0, 7.0])
        result = u - v
        assert result == Vector([-3.0, -4.0])

    def test_subtract_self_is_zero(self) -> None:
        u = Vector([4.0, -2.5, 0.0])
        result = u - u
        assert result == Vector([0.0, 0.0, 0.0])

    def test_empty_vectors(self) -> None:
        u = Vector([])
        v = Vector([])
        result = u - v
        assert result == Vector([])

    def test_single_element(self) -> None:
        u = Vector([42.0])
        v = Vector([10.0])
        assert u - v == Vector([32.0])

    def test_anti_commutativity(self) -> None:
        u = Vector([1.5, 2.5, 3.5])
        v = Vector([4.0, 5.0, 6.0])
        assert (u - v) == Vector([-2.5, -2.5, -2.5])
        assert (v - u) == Vector([2.5, 2.5, 2.5])

    def test_immutability(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([3.0, 4.0])
        _ = u - v
        assert u == Vector([1.0, 2.0])
        assert v == Vector([3.0, 4.0])

    def test_dimension_mismatch_raises_value_error(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([1.0, 2.0, 3.0])
        err_msg = "cannot subtract vectors of different lengths"
        with pytest.raises(ValueError, match=err_msg):
            _ = u - v

    def test_empty_and_non_empty_mismatch(self) -> None:
        u = Vector([])
        v = Vector([1.0])
        err_msg = "cannot subtract vectors of different lengths"
        with pytest.raises(ValueError, match=err_msg):
            _ = u - v

    def test_invalid_type_raises_type_error(self) -> None:
        u = Vector([1.0, 2.0])
        with pytest.raises(TypeError):
            _ = u - 42  # type: ignore[operator]
        with pytest.raises(TypeError):
            _ = u - [1.0, 2.0]  # type: ignore[operator]


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
        m1 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        m2 = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
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


class TestMatrixSub:
    def test_basic_subtraction_square(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[7.0, 4.0], [-2.0, 2.0]])
        result = m1 - m2
        assert result == Matrix([[-6.0, -2.0], [5.0, 2.0]])

    def test_subtract_self_is_zero(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        assert m - m == Matrix([[0.0, 0.0], [0.0, 0.0]])

    def test_rectangular_matrix_subtraction(self) -> None:
        m1 = Matrix([[10.0, 20.0, 30.0], [40.0, 50.0, 60.0]])
        m2 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        result = m1 - m2
        assert result == Matrix([[9.0, 18.0, 27.0], [36.0, 45.0, 54.0]])

    def test_single_element_matrix(self) -> None:
        m1 = Matrix([[5.0]])
        m2 = Matrix([[-2.0]])
        assert m1 - m2 == Matrix([[7.0]])

    def test_anti_commutativity(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[5.0, 6.0], [7.0, 8.0]])
        assert (m1 - m2) == Matrix([[-4.0, -4.0], [-4.0, -4.0]])
        assert (m2 - m1) == Matrix([[4.0, 4.0], [4.0, 4.0]])

    def test_immutability(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[5.0, 6.0], [7.0, 8.0]])
        _ = m1 - m2
        assert m1 == Matrix([[1.0, 2.0], [3.0, 4.0]])
        assert m2 == Matrix([[5.0, 6.0], [7.0, 8.0]])

    def test_shape_mismatch_different_rows(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[1.0, 2.0]])
        err_msg = "cannot subtract matrices of different shapes"
        with pytest.raises(ValueError, match=err_msg):
            _ = m1 - m2

    def test_shape_mismatch_different_cols(self) -> None:
        m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
        m2 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        err_msg = "cannot subtract matrices of different shapes"
        with pytest.raises(ValueError, match=err_msg):
            _ = m1 - m2

    def test_shape_mismatch_transposed_dimensions(self) -> None:
        m1 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        m2 = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        err_msg = "cannot subtract matrices of different shapes"
        with pytest.raises(ValueError, match=err_msg):
            _ = m1 - m2

    def test_invalid_type_raises_type_error(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Vector([1.0, 2.0])
        with pytest.raises(TypeError):
            _ = m - 42  # type: ignore[operator]
        with pytest.raises(TypeError):
            _ = m - v  # type: ignore[operator]


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
