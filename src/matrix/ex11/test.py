import pytest
from matrix import Matrix


class TestMatrixDeterminant:
    def test_subject_example_2x2_singular(self) -> None:
        u = Matrix([[1.0, -1.0], [-1.0, 1.0]])
        assert u.determinant() == pytest.approx(0.0, abs=1e-6)

    def test_subject_example_3x3_diagonal(self) -> None:
        u = Matrix([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
        assert u.determinant() == pytest.approx(8.0)

    def test_subject_example_3x3_general(self) -> None:
        u = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
        assert u.determinant() == pytest.approx(-174.0)

    def test_subject_example_4x4_general(self) -> None:
        u = Matrix(
            [
                [8.0, 5.0, -2.0, 4.0],
                [4.0, 2.5, 20.0, 4.0],
                [8.0, 5.0, 1.0, 4.0],
                [28.0, -4.0, 17.0, 1.0],
            ]
        )
        assert u.determinant() == pytest.approx(1032.0)

    def test_identity_matrix(self) -> None:
        u = Matrix([[1.0, 0.0], [0.0, 1.0]])
        assert u.determinant() == pytest.approx(1.0)

    def test_single_element_matrix(self) -> None:
        assert Matrix([[42.5]]).determinant() == pytest.approx(42.5)

    def test_empty_matrix(self) -> None:
        assert Matrix([]).determinant() == pytest.approx(1.0)

    def test_row_swap_flips_sign(self) -> None:
        # Swapping two rows of a matrix negates its determinant.
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        swapped = Matrix([[3.0, 4.0], [1.0, 2.0]])
        assert swapped.determinant() == pytest.approx(-u.determinant())

    def test_zero_row_gives_zero_determinant(self) -> None:
        u = Matrix([[1.0, 2.0, 3.0], [0.0, 0.0, 0.0], [7.0, 8.0, 9.0]])
        assert u.determinant() == pytest.approx(0.0, abs=1e-6)

    def test_linearly_dependent_rows(self) -> None:
        u = Matrix([[1.0, 2.0], [2.0, 4.0]])
        assert u.determinant() == pytest.approx(0.0, abs=1e-6)

    def test_immutability(self) -> None:
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        _ = u.determinant()
        assert u == Matrix([[1.0, 2.0], [3.0, 4.0]])

    def test_non_square_matrix_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            _ = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]).determinant()
        with pytest.raises(ValueError):
            _ = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]).determinant()
