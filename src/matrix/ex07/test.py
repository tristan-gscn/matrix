import pytest
from matrix import Matrix, Vector


class TestMatrixMulVec:
    def test_subject_example_identity(self) -> None:
        u = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v = Vector([4.0, 2.0])
        assert u.mul_vec(v) == Vector([4.0, 2.0])
        assert u * v == Vector([4.0, 2.0])

    def test_subject_example_scaled_identity(self) -> None:
        u = Matrix([[2.0, 0.0], [0.0, 2.0]])
        v = Vector([4.0, 2.0])
        assert u.mul_vec(v) == Vector([8.0, 4.0])
        assert u * v == Vector([8.0, 4.0])

    def test_subject_example_general(self) -> None:
        u = Matrix([[2.0, -2.0], [-2.0, 2.0]])
        v = Vector([4.0, 2.0])
        assert u.mul_vec(v) == Vector([4.0, -4.0])
        assert u * v == Vector([4.0, -4.0])

    def test_rectangular_matrix_by_vector(self) -> None:
        # 2x3 matrix * 3D vector -> 2D vector
        m = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        v = Vector([10.0, 20.0, 30.0])
        # [1*10 + 2*20 + 3*30, 4*10 + 5*20 + 6*30] = [140.0, 320.0]
        assert m.mul_vec(v) == Vector([140.0, 320.0])
        assert m * v == Vector([140.0, 320.0])

    def test_zero_vector(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Vector([0.0, 0.0])
        assert m.mul_vec(v) == Vector([0.0, 0.0])

    def test_immutability(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Vector([5.0, 6.0])
        _ = m.mul_vec(v)
        assert m == Matrix([[1.0, 2.0], [3.0, 4.0]])
        assert v == Vector([5.0, 6.0])

    def test_dimension_mismatch_raises_value_error(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])  # 2 cols
        v = Vector([1.0, 2.0, 3.0])  # 3 elements
        with pytest.raises(ValueError):
            _ = m.mul_vec(v)
        with pytest.raises(ValueError):
            _ = m * v


class TestMatrixMulMat:
    def test_subject_example_identity_by_identity(self) -> None:
        u = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v = Matrix([[1.0, 0.0], [0.0, 1.0]])
        expected = Matrix([[1.0, 0.0], [0.0, 1.0]])
        assert u.mul_mat(v) == expected
        assert u * v == expected

    def test_subject_example_identity_by_general(self) -> None:
        u = Matrix([[1.0, 0.0], [0.0, 1.0]])
        v = Matrix([[2.0, 1.0], [4.0, 2.0]])
        expected = Matrix([[2.0, 1.0], [4.0, 2.0]])
        assert u.mul_mat(v) == expected
        assert u * v == expected

    def test_subject_example_general(self) -> None:
        u = Matrix([[3.0, -5.0], [6.0, 8.0]])
        v = Matrix([[2.0, 1.0], [4.0, 2.0]])
        expected = Matrix([[-14.0, -7.0], [44.0, 22.0]])
        assert u.mul_mat(v) == expected
        assert u * v == expected

    def test_rectangular_matrices(self) -> None:
        # 2x3 matrix * 3x2 matrix -> 2x2 matrix
        a = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        b = Matrix([[7.0, 8.0], [9.0, 1.0], [2.0, 3.0]])
        expected = Matrix([[31.0, 19.0], [85.0, 55.0]])
        assert a.mul_mat(b) == expected
        assert a * b == expected

    def test_associativity(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[5.0, 6.0], [7.0, 8.0]])
        c = Matrix([[9.0, 1.0], [2.0, 3.0]])
        assert (a * b) * c == a * (b * c)

    def test_distributivity_over_addition(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[5.0, 6.0], [7.0, 8.0]])
        c = Matrix([[1.0, -1.0], [2.0, -2.0]])
        assert a * (b + c) == (a * b) + (a * c)

    def test_non_commutativity(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[2.0, 0.0], [1.0, 2.0]])
        assert a * b != b * a

    def test_immutability(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[5.0, 6.0], [7.0, 8.0]])
        _ = a.mul_mat(b)
        assert a == Matrix([[1.0, 2.0], [3.0, 4.0]])
        assert b == Matrix([[5.0, 6.0], [7.0, 8.0]])

    def test_dimension_mismatch_raises_value_error(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])  # 2x2
        b = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])  # 3x2
        with pytest.raises(ValueError):
            _ = a.mul_mat(b)
        with pytest.raises(ValueError):
            _ = a * b

    def test_unsupported_type_raises_type_error(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        with pytest.raises(TypeError):
            _ = m * "invalid"  # type: ignore[operator]
        with pytest.raises(TypeError):
            _ = m * [1.0, 2.0]  # type: ignore[operator]
