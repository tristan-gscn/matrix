import pytest
from matrix import Vector
from matrix.ex01.linear_combination import linear_combination


class TestLinearCombination:
    def test_subject_example_canonical_basis(self) -> None:
        e1 = Vector([1.0, 0.0, 0.0])
        e2 = Vector([0.0, 1.0, 0.0])
        e3 = Vector([0.0, 0.0, 1.0])
        result = linear_combination([e1, e2, e3], [10.0, -2.0, 0.5])
        assert result == Vector([10.0, -2.0, 0.5])

    def test_subject_example_general_vectors(self) -> None:
        v1 = Vector([1.0, 2.0, 3.0])
        v2 = Vector([0.0, 10.0, -100.0])
        result = linear_combination([v1, v2], [10.0, -2.0])
        assert result == Vector([10.0, 0.0, 230.0])

    def test_single_vector(self) -> None:
        v = Vector([3.0, -4.0])
        assert linear_combination([v], [2.5]) == Vector([7.5, -10.0])

    def test_zero_coefficients(self) -> None:
        v1 = Vector([1.0, 2.0])
        v2 = Vector([3.0, 4.0])
        assert linear_combination([v1, v2], [0.0, 0.0]) == Vector([0.0, 0.0])

    def test_empty_lists(self) -> None:
        assert linear_combination([], []) == Vector([])

    def test_immutability(self) -> None:
        v1 = Vector([1.0, 2.0])
        v2 = Vector([3.0, 4.0])
        _ = linear_combination([v1, v2], [2.0, 3.0])
        assert v1 == Vector([1.0, 2.0])
        assert v2 == Vector([3.0, 4.0])

    def test_count_mismatch_raises_value_error(self) -> None:
        v1 = Vector([1.0, 2.0])
        v2 = Vector([3.0, 4.0])
        err_msg = "number of vectors and coefficients must match"
        with pytest.raises(ValueError, match=err_msg):
            _ = linear_combination([v1, v2], [1.0])
        with pytest.raises(ValueError, match=err_msg):
            _ = linear_combination([v1], [1.0, 2.0])

    def test_incoherent_dimensions_raises_value_error(self) -> None:
        v1 = Vector([1.0, 2.0])
        v2 = Vector([1.0, 2.0, 3.0])
        err_msg = "incoherent vector dimension"
        with pytest.raises(ValueError, match=err_msg):
            _ = linear_combination([v1, v2], [1.0, 2.0])

    def test_non_vector_raises_type_error(self) -> None:
        v = Vector([1.0, 2.0])
        bad_list: list[object] = [v, 42]
        with pytest.raises(TypeError):
            _ = linear_combination(bad_list, [1.0, 2.0])  # type: ignore

    def test_non_number_coef_raises_type_error(self) -> None:
        v = Vector([1.0, 2.0])
        bad_coefs: list[object] = ["invalid"]
        with pytest.raises(TypeError):
            _ = linear_combination([v], bad_coefs)  # type: ignore
