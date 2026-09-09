import pytest
from matrix import Matrix


class TestMatrixInverse:
    def test_identity_helper(self) -> None:
        expected = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        assert Matrix.identity(3) == expected

    def test_subject_example_identity_3x3(self) -> None:
        u = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        assert u.inverse() == u

    def test_subject_example_scaled_identity_3x3(self) -> None:
        u = Matrix([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        expected = Matrix([[0.5, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]])
        assert u.inverse() == expected

    def test_subject_example_3x3_general(self) -> None:
        u = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
        expected = Matrix(
            [
                [0.649425287, 0.097701149, -0.655172414],
                [-0.781609195, -0.126436782, 0.965517241],
                [0.143678161, 0.074712644, -0.206896552],
            ]
        )
        assert u.inverse() == expected

    def test_inverse_times_matrix_is_identity(self) -> None:
        u = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
        identity = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        assert (u * u.inverse()) == identity
        assert (u.inverse() * u) == identity

    def test_single_element_matrix(self) -> None:
        assert Matrix([[4.0]]).inverse() == Matrix([[0.25]])

    def test_empty_matrix(self) -> None:
        assert Matrix([]).inverse() == Matrix([])

    def test_immutability(self) -> None:
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        _ = u.inverse()
        assert u == Matrix([[1.0, 2.0], [3.0, 4.0]])

    def test_singular_matrix_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            _ = Matrix([[1.0, 2.0], [2.0, 4.0]]).inverse()

    def test_non_square_matrix_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            _ = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]).inverse()
