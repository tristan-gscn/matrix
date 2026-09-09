from matrix import Matrix


class TestMatrixRowEchelon:
    def test_subject_example_identity_3x3(self) -> None:
        u = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        expected = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        assert u.row_echelon() == expected

    def test_subject_example_invertible_2x2(self) -> None:
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        expected = Matrix([[1.0, 0.0], [0.0, 1.0]])
        assert u.row_echelon() == expected

    def test_subject_example_singular_2x2(self) -> None:
        u = Matrix([[1.0, 2.0], [2.0, 4.0]])
        expected = Matrix([[1.0, 2.0], [0.0, 0.0]])
        assert u.row_echelon() == expected

    def test_subject_example_rectangular_3x5(self) -> None:
        u = Matrix(
            [
                [8.0, 5.0, -2.0, 4.0, 28.0],
                [4.0, 2.5, 20.0, 4.0, -4.0],
                [8.0, 5.0, 1.0, 4.0, 17.0],
            ]
        )
        expected = Matrix(
            [
                [1.0, 0.625, 0.0, 0.0, -73.0 / 6.0],
                [0.0, 0.0, 1.0, 0.0, -11.0 / 3.0],
                [0.0, 0.0, 0.0, 1.0, 29.5],
            ]
        )
        assert u.row_echelon() == expected

    def test_zero_matrix(self) -> None:
        u = Matrix([[0.0, 0.0], [0.0, 0.0]])
        assert u.row_echelon() == Matrix([[0.0, 0.0], [0.0, 0.0]])

    def test_single_element_non_zero(self) -> None:
        u = Matrix([[5.0]])
        assert u.row_echelon() == Matrix([[1.0]])

    def test_single_element_zero(self) -> None:
        u = Matrix([[0.0]])
        assert u.row_echelon() == Matrix([[0.0]])

    def test_empty_matrix(self) -> None:
        u = Matrix([])
        assert u.row_echelon() == Matrix([])

    def test_pivot_needs_row_swap(self) -> None:
        # First row has 0 in column 0, must swap with second row
        u = Matrix([[0.0, 2.0], [3.0, 1.0]])
        expected = Matrix([[1.0, 0.0], [0.0, 1.0]])
        assert u.row_echelon() == expected

    def test_tall_matrix_3x2(self) -> None:
        u = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
        expected = Matrix([[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]])
        assert u.row_echelon() == expected

    def test_idempotence(self) -> None:
        # rref(rref(A)) == rref(A)
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        rref1 = u.row_echelon()
        rref2 = rref1.row_echelon()
        assert rref1 == rref2

    def test_immutability(self) -> None:
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        _ = u.row_echelon()
        assert u == Matrix([[1.0, 2.0], [3.0, 4.0]])

    def test_reduce_false_gives_plain_echelon_form(self) -> None:
        # Without reduction: pivots keep their natural value (not
        # normalized to 1) and rows above a pivot are left untouched.
        u = Matrix([[2.0, 4.0], [3.0, 1.0]])
        expected = Matrix([[3.0, 1.0], [0.0, 10.0 / 3.0]])
        assert u.row_echelon(reduce=False) == expected

    def test_reduce_true_is_the_default(self) -> None:
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        assert u.row_echelon() == u.row_echelon(reduce=True)
