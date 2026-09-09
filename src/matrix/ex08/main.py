from matrix import Matrix


def demo_subject_examples() -> None:
    print("--- [ex08] Subject examples ---")
    u1 = Matrix([[1.0, 0.0], [0.0, 1.0]])
    print(f"u1 ={u1}")
    print(f"u1.trace() = {u1.trace()}")

    u2 = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
    print(f"\nu2 ={u2}")
    print(f"u2.trace() = {u2.trace()}")

    u3 = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]])
    print(f"\nu3 ={u3}")
    print(f"u3.trace() = {u3.trace()}")


def demo_properties() -> None:
    print("\n--- [ex08] Trace algebraic properties ---")
    a = Matrix([[1.0, 2.0], [3.0, 4.0]])
    b = Matrix([[5.0, 6.0], [7.0, 8.0]])
    print(f"A ={a}\nB ={b}")
    print(f"tr(A + B) = {(a + b).trace()}")
    print(f"tr(A) + tr(B) = {a.trace() + b.trace()}")
    print(f"tr(A * B) = {(a * b).trace()}")
    print(f"tr(B * A) = {(b * a).trace()}")


def demo_errors() -> None:
    print("\n--- [ex08] Error handling demonstrations ---")
    try:
        m = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        _ = m.trace()
    except ValueError as e:
        print(f"Caught expected non-square matrix error: {e}")


def main() -> None:
    print("========================================")
    print("           Exercise 08: Trace           ")
    print("========================================")
    demo_subject_examples()
    demo_properties()
    demo_errors()


if __name__ == "__main__":
    main()
