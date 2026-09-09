from matrix import Matrix


class TestMatrixRank:
    def test_subject_example_identity_3x3(self) -> None:
        u = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        assert u.rank() == 3

    def test_subject_example_dependent_columns(self) -> None:
        u = Matrix(
            [
                [1.0, 2.0, 0.0, 0.0],
                [2.0, 4.0, 0.0, 0.0],
                [-1.0, 2.0, 1.0, 1.0],
            ]
        )
        assert u.rank() == 2

    def test_subject_example_tall_full_column_rank(self) -> None:
        u = Matrix(
            [
                [8.0, 5.0, -2.0],
                [4.0, 7.0, 20.0],
                [7.0, 6.0, 1.0],
                [21.0, 18.0, 7.0],
            ]
        )
        assert u.rank() == 3

    def test_zero_matrix(self) -> None:
        assert Matrix([[0.0, 0.0], [0.0, 0.0]]).rank() == 0

    def test_empty_matrix(self) -> None:
        assert Matrix([]).rank() == 0

    def test_singular_square_matrix(self) -> None:
        assert Matrix([[1.0, 2.0], [2.0, 4.0]]).rank() == 1

    def test_immutability(self) -> None:
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        _ = u.rank()
        assert u == Matrix([[1.0, 2.0], [3.0, 4.0]])
