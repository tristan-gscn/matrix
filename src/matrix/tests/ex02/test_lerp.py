import pytest
from matrix import Matrix, Vector, lerp


class TestLerp:
    def test_scalar_subject_examples(self) -> None:
        assert lerp(0.0, 1.0, 0.0) == 0.0
        assert lerp(0.0, 1.0, 1.0) == 1.0
        assert lerp(0.0, 1.0, 0.5) == 0.5
        assert lerp(21.0, 42.0, 0.3) == pytest.approx(27.3)

    def test_scalar_int_inputs(self) -> None:
        assert lerp(0, 10, 0.5) == 5.0
        assert isinstance(lerp(0, 10, 0.5), float)

    def test_scalar_extrapolation(self) -> None:
        assert lerp(0.0, 10.0, 1.5) == 15.0
        assert lerp(0.0, 10.0, -0.5) == -5.0

    def test_vector_subject_example(self) -> None:
        u = Vector([2.0, 1.0])
        v = Vector([4.0, 2.0])
        expected = Vector([2.6, 1.3])
        result = lerp(u, v, 0.3)
        assert result == expected

    def test_vector_boundary_values(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([10.0, 20.0])
        assert lerp(u, v, 0.0) == u
        assert lerp(u, v, 1.0) == v
        assert lerp(u, v, 0.5) == Vector([5.5, 11.0])

    def test_matrix_subject_example(self) -> None:
        u = Matrix([[2.0, 1.0], [3.0, 4.0]])
        v = Matrix([[20.0, 10.0], [30.0, 40.0]])
        expected = Matrix([[11.0, 5.5], [16.5, 22.0]])
        assert lerp(u, v, 0.5) == expected

    def test_matrix_boundary_values(self) -> None:
        u = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Matrix([[5.0, 6.0], [7.0, 8.0]])
        assert lerp(u, v, 0.0) == u
        assert lerp(u, v, 1.0) == v

    def test_immutability(self) -> None:
        u = Vector([2.0, 1.0])
        v = Vector([4.0, 2.0])
        _ = lerp(u, v, 0.3)
        assert u == Vector([2.0, 1.0])
        assert v == Vector([4.0, 2.0])

    def test_type_mismatch_raises_type_error(self) -> None:
        with pytest.raises(TypeError):
            _ = lerp(1.0, Vector([1.0]), 0.5)  # type: ignore[type-var]

    def test_vector_dimension_mismatch_raises_value_error(self) -> None:
        u = Vector([1.0, 2.0])
        v = Vector([1.0, 2.0, 3.0])
        with pytest.raises(ValueError):
            _ = lerp(u, v, 0.5)

    def test_matrix_shape_mismatch_raises_value_error(self) -> None:
        u = Matrix([[1.0, 2.0]])
        v = Matrix([[1.0, 2.0], [3.0, 4.0]])
        with pytest.raises(ValueError):
            _ = lerp(u, v, 0.5)

    def test_invalid_t_raises_type_error(self) -> None:
        with pytest.raises(TypeError):
            _ = lerp(1.0, 2.0, "invalid")  # type: ignore[arg-type]
