from matrix import Vector


class TestVectorNorm1:
    def test_subject_example_zeros(self) -> None:
        u = Vector([0.0, 0.0, 0.0])
        assert u.norm_1() == 0.0

    def test_subject_example_positive(self) -> None:
        u = Vector([1.0, 2.0, 3.0])
        assert u.norm_1() == 6.0

    def test_subject_example_negative(self) -> None:
        u = Vector([-1.0, -2.0])
        assert u.norm_1() == 3.0

    def test_mixed_signs(self) -> None:
        u = Vector([-4.0, 2.5, -0.5])
        assert u.norm_1() == 7.0

    def test_negative_zero(self) -> None:
        u = Vector([-0.0, 0.0])
        assert u.norm_1() == 0.0

    def test_empty_vector(self) -> None:
        u = Vector([])
        assert u.norm_1() == 0.0

    def test_immutability(self) -> None:
        u = Vector([1.0, -2.0])
        _ = u.norm_1()
        assert u == Vector([1.0, -2.0])
