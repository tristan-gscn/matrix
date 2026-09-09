from matrix import Matrix


def demo_subject_examples() -> None:
    print("--- [ex12] Subject examples ---")
    u1 = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    print(f"u1 ={u1}")
    print(f"u1.inverse() ={u1.inverse()}")

    u2 = Matrix([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
    print(f"\nu2 ={u2}")
    print(f"u2.inverse() ={u2.inverse()}")

    u3 = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
    print(f"\nu3 ={u3}")
    print(f"u3.inverse() ={u3.inverse()}")


def demo_properties() -> None:
    print("\n--- [ex12] Inverse properties ---")
    a = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
    print(f"A ={a}")
    print(f"A * A^-1 ={a * a.inverse()}")
    print(f"A^-1 * A ={a.inverse() * a}")


def demo_errors() -> None:
    print("\n--- [ex12] Error handling demonstrations ---")
    try:
        m = Matrix([[1.0, 2.0], [2.0, 4.0]])
        _ = m.inverse()
    except ValueError as e:
        print(f"Caught expected singular matrix error: {e}")

    try:
        m = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        _ = m.inverse()
    except ValueError as e:
        print(f"Caught expected non-square matrix error: {e}")


def main() -> None:
    print("========================================")
    print("          Exercise 12: Inverse          ")
    print("========================================")
    demo_subject_examples()
    demo_properties()
    demo_errors()


if __name__ == "__main__":
    main()
