from matrix import Vector


class TestVectorNormInf:
    def test_subject_example_zeros(self) -> None:
        u = Vector([0.0, 0.0, 0.0])
        assert u.norm_inf() == 0.0

    def test_subject_example_positive(self) -> None:
        u = Vector([1.0, 2.0, 3.0])
        assert u.norm_inf() == 3.0

    def test_subject_example_negative(self) -> None:
        u = Vector([-1.0, -2.0])
        assert u.norm_inf() == 2.0

    def test_supremum_selection(self) -> None:
        u = Vector([-42.0, 10.0, 25.0])
        assert u.norm_inf() == 42.0

    def test_negative_zero(self) -> None:
        u = Vector([-0.0, 0.0])
        assert u.norm_inf() == 0.0

    def test_empty_vector(self) -> None:
        u = Vector([])
        assert u.norm_inf() == 0.0

    def test_immutability(self) -> None:
        u = Vector([1.0, -5.0])
        _ = u.norm_inf()
        assert u == Vector([1.0, -5.0])
