from matrix import Matrix


def demo_subject_examples() -> None:
    print("--- [ex11] Subject examples ---")
    u1 = Matrix([[1.0, -1.0], [-1.0, 1.0]])
    print(f"u1 ={u1}")
    print(f"u1.determinant() = {u1.determinant()}")

    u2 = Matrix([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
    print(f"\nu2 ={u2}")
    print(f"u2.determinant() = {u2.determinant()}")

    u3 = Matrix([[8.0, 5.0, -2.0], [4.0, 7.0, 20.0], [7.0, 6.0, 1.0]])
    print(f"\nu3 ={u3}")
    print(f"u3.determinant() = {u3.determinant()}")

    u4 = Matrix(
        [
            [8.0, 5.0, -2.0, 4.0],
            [4.0, 2.5, 20.0, 4.0],
            [8.0, 5.0, 1.0, 4.0],
            [28.0, -4.0, 17.0, 1.0],
        ]
    )
    print(f"\nu4 ={u4}")
    print(f"u4.determinant() = {u4.determinant()}")


def demo_properties() -> None:
    print("\n--- [ex11] Determinant properties ---")
    a = Matrix([[1.0, 2.0], [3.0, 4.0]])
    swapped = Matrix([[3.0, 4.0], [1.0, 2.0]])
    print(f"A ={a}")
    print(f"det(A) = {a.determinant()}")
    print(f"Row swap negates det: det(swap(A)) = {swapped.determinant()}")

    singular = Matrix([[1.0, 2.0], [2.0, 4.0]])
    print(f"\nSingular matrix ={singular}")
    print(f"det(singular) = {singular.determinant()}")


def demo_errors() -> None:
    print("\n--- [ex11] Error handling demonstrations ---")
    try:
        m = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        _ = m.determinant()
    except ValueError as e:
        print(f"Caught expected non-square matrix error: {e}")


def main() -> None:
    print("========================================")
    print("        Exercise 11: Determinant        ")
    print("========================================")
    demo_subject_examples()
    demo_properties()
    demo_errors()


if __name__ == "__main__":
    main()
