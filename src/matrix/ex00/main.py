"""Exercise 00 - Add, Subtract and Scale."""

from matrix._core import Matrix, Vector


def demo_vectors() -> None:
    print("--- [ex00] Vector demonstrations ---")
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    print(f"u ={u}\nv ={v}")

    print(f"u + v ={u + v}")
    print(f"u - v ={u - v}")
    print(f"u * 2.0 ={u * 2.0}")


def demo_matrices() -> None:
    print("\n--- [ex00] Matrix demonstrations ---")
    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    print(f"u ={u}\nv ={v}")

    print(f"u + v ={u + v}")
    print(f"u - v ={u - v}")
    print(f"u * 2.0 ={u * 2.0}")


def demo_errors() -> None:
    print("\n--- [ex00] Error handling demonstrations ---")
    try:
        _ = Vector([1.0, 2.0]) + Vector([1.0, 2.0, 3.0])
    except ValueError as e:
        print(f"Caught expected Vector dimension mismatch: {e}")

    try:
        _ = Matrix([[1.0, 2.0]]) + Matrix([[1.0, 2.0], [3.0, 4.0]])
    except ValueError as e:
        print(f"Caught expected Matrix shape mismatch: {e}")


def main() -> None:
    print("========================================")
    print("      Exercise 00: Add, Sub, Scale      ")
    print("========================================")
    demo_vectors()
    demo_matrices()
    demo_errors()


if __name__ == "__main__":
    main()
