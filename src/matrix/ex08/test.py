import pytest
from matrix import Matrix


class TestMatrixTrace:
    def test_subject_example_2x2_identity(self) -> None:
        u = Matrix([[1.0, 0.0], [0.0, 1.0]])
        assert u.trace() == 2.0

    def test_subject_example_3x3_general(self) -> None:
        u = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
        assert u.trace() == 9.0

    def test_subject_example_3x3_negative(self) -> None:
        u = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]])
        assert u.trace() == -21.0

    def test_single_element_matrix(self) -> None:
        u = Matrix([[42.5]])
        assert u.trace() == 42.5

    def test_empty_matrix(self) -> None:
        u = Matrix([])
        assert u.trace() == 0.0

    def test_linearity_addition(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[5.0, 6.0], [7.0, 8.0]])
        assert (a + b).trace() == pytest.approx(a.trace() + b.trace())

    def test_linearity_scaling(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        scalar = 3.5
        assert (a * scalar).trace() == pytest.approx(scalar * a.trace())

    def test_cyclic_commutativity(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[2.0, 0.0], [1.0, 2.0]])
        assert (a * b).trace() == pytest.approx((b * a).trace())

    def test_immutability(self) -> None:
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        _ = u.trace()
        assert u == Matrix([[1.0, 2.0], [3.0, 4.0]])

    def test_non_square_matrix_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            _ = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]).trace()
        with pytest.raises(ValueError):
            _ = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]).trace()
