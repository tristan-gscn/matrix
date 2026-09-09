from matrix._core import Vector


def demo_subject_examples() -> None:
    print("--- [ex04] Subject examples ---")
    u1 = Vector([0.0, 0.0, 0.0])
    print(f"u1 ={u1}")
    print(
        f"u1.norm_1() = {u1.norm_1()}, "
        f"u1.norm() = {u1.norm()}, "
        f"u1.norm_inf() = {u1.norm_inf()}"
    )

    u2 = Vector([1.0, 2.0, 3.0])
    print(f"\nu2 ={u2}")
    print(
        f"u2.norm_1() = {u2.norm_1()}, "
        f"u2.norm() = {u2.norm():.8f}, "
        f"u2.norm_inf() = {u2.norm_inf()}"
    )

    u3 = Vector([-1.0, -2.0])
    print(f"\nu3 ={u3}")
    print(
        f"u3.norm_1() = {u3.norm_1()}, "
        f"u3.norm() = {u3.norm():.9f}, "
        f"u3.norm_inf() = {u3.norm_inf()}"
    )


def demo_edge_cases() -> None:
    print("\n--- [ex04] Edge cases ---")
    u_empty = Vector([])
    print("Empty vector Vector([]):")
    print(
        f"norm_1() = {u_empty.norm_1()}, "
        f"norm() = {u_empty.norm()}, "
        f"norm_inf() = {u_empty.norm_inf()}"
    )

    u_neg_zero = Vector([-0.0, 0.0])
    print(f"\nVector with -0.0 {u_neg_zero}:")
    print(
        f"norm_1() = {u_neg_zero.norm_1()}, "
        f"norm() = {u_neg_zero.norm()}, "
        f"norm_inf() = {u_neg_zero.norm_inf()}"
    )


def main() -> None:
    print("========================================")
    print("           Exercise 04: Norm            ")
    print("========================================")
    demo_subject_examples()
    demo_edge_cases()


if __name__ == "__main__":
    main()
