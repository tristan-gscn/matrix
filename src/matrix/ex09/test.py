from matrix import Matrix


class TestMatrixTranspose:
    def test_rectangular_2x3(self) -> None:
        m = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        expected = Matrix([[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]])
        assert m.transpose() == expected
        assert m.transpose().shape() == (3, 2)

    def test_rectangular_3x2(self) -> None:
        m = Matrix([[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]])
        expected = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        assert m.transpose() == expected
        assert m.transpose().shape() == (2, 3)

    def test_square_matrix(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        expected = Matrix([[1.0, 3.0], [2.0, 4.0]])
        assert m.transpose() == expected

    def test_single_element_matrix(self) -> None:
        m = Matrix([[42.0]])
        assert m.transpose() == Matrix([[42.0]])

    def test_empty_matrix(self) -> None:
        m = Matrix([])
        assert m.transpose() == Matrix([])
        assert m.transpose().shape() == (0, 0)

    def test_row_matrix(self) -> None:
        m = Matrix([[1.0, 2.0, 3.0]])
        expected = Matrix([[1.0], [2.0], [3.0]])
        assert m.transpose() == expected
        assert m.transpose().shape() == (3, 1)

    def test_column_matrix(self) -> None:
        m = Matrix([[1.0], [2.0], [3.0]])
        expected = Matrix([[1.0, 2.0, 3.0]])
        assert m.transpose() == expected
        assert m.transpose().shape() == (1, 3)

    def test_involution_property(self) -> None:
        m = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        assert m.transpose().transpose() == m

    def test_linearity_addition(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        b = Matrix([[5.0, 6.0], [7.0, 8.0]])
        assert (a + b).transpose() == a.transpose() + b.transpose()

    def test_linearity_scaling(self) -> None:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])
        scalar = 2.5
        assert (a * scalar).transpose() == a.transpose() * scalar

    def test_product_reversal_property(self) -> None:
        a = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        b = Matrix([[7.0, 8.0], [9.0, 1.0], [2.0, 3.0]])
        assert (a * b).transpose() == b.transpose() * a.transpose()

    def test_trace_invariance(self) -> None:
        a = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
        assert a.transpose().trace() == a.trace()

    def test_symmetric_matrix(self) -> None:
        sym = Matrix([[1.0, 7.0, 3.0], [7.0, 4.0, -5.0], [3.0, -5.0, 6.0]])
        assert sym.transpose() == sym

    def test_immutability(self) -> None:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        _ = m.transpose()
        assert m == Matrix([[1.0, 2.0], [3.0, 4.0]])
