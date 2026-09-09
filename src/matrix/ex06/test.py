import pytest
from matrix import Vector
from matrix.ex06.cross_product import cross_product


class TestCrossProduct:
    def test_subject_example_canonical_z_x(self) -> None:
        u = Vector([0.0, 0.0, 1.0])
        v = Vector([1.0, 0.0, 0.0])
        assert cross_product(u, v) == Vector([0.0, 1.0, 0.0])

    def test_subject_example_consecutive_integers(self) -> None:
        u = Vector([1.0, 2.0, 3.0])
        v = Vector([4.0, 5.0, 6.0])
        assert cross_product(u, v) == Vector([-3.0, 6.0, -3.0])

    def test_subject_example_general(self) -> None:
        u = Vector([4.0, 2.0, -3.0])
        v = Vector([-2.0, -5.0, 16.0])
        assert cross_product(u, v) == Vector([17.0, -58.0, -16.0])

    def test_canonical_basis_cyclic(self) -> None:
        i = Vector([1.0, 0.0, 0.0])
        j = Vector([0.0, 1.0, 0.0])
        k = Vector([0.0, 0.0, 1.0])

        assert cross_product(i, j) == k
        assert cross_product(j, k) == i
        assert cross_product(k, i) == j

    def test_anticommutativity(self) -> None:
        u = Vector([1.5, -2.0, 3.0])
        v = Vector([4.0, 0.5, -1.0])
        assert cross_product(u, v) == cross_product(v, u) * -1.0

    def test_self_cross_product_is_zero(self) -> None:
        u = Vector([3.0, -5.0, 7.0])
        assert cross_product(u, u) == Vector([0.0, 0.0, 0.0])

    def test_orthogonality_to_operands(self) -> None:
        u = Vector([2.0, 3.0, 4.0])
        v = Vector([5.0, 6.0, 7.0])
        w = cross_product(u, v)
        assert w.dot(u) == pytest.approx(0.0)
        assert w.dot(v) == pytest.approx(0.0)

    def test_immutability(self) -> None:
        u = Vector([1.0, 2.0, 3.0])
        v = Vector([4.0, 5.0, 6.0])
        _ = cross_product(u, v)
        assert u == Vector([1.0, 2.0, 3.0])
        assert v == Vector([4.0, 5.0, 6.0])

    def test_invalid_dimension_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            _ = cross_product(Vector([1.0, 2.0]), Vector([3.0, 4.0]))
        with pytest.raises(ValueError):
            _ = cross_product(
                Vector([1.0, 2.0, 3.0, 4.0]), Vector([1.0, 2.0, 3.0, 4.0])
            )
        with pytest.raises(ValueError):
            _ = cross_product(Vector([]), Vector([]))
        with pytest.raises(ValueError):
            _ = cross_product(Vector([1.0, 2.0, 3.0]), Vector([1.0, 2.0]))
