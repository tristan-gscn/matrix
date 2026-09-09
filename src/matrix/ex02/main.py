from matrix._core import Matrix, Vector
from matrix.ex02.lerp import lerp


def demo_scalars() -> None:
    print("--- [ex02] Scalar demonstrations ---")
    print(f"lerp(0.0, 1.0, 0.0) = {lerp(0.0, 1.0, 0.0)}")
    print(f"lerp(0.0, 1.0, 1.0) = {lerp(0.0, 1.0, 1.0)}")
    print(f"lerp(0.0, 1.0, 0.5) = {lerp(0.0, 1.0, 0.5)}")
    print(f"lerp(21.0, 42.0, 0.3) = {round(lerp(21.0, 42.0, 0.3), 6)}")
    print(f"lerp(0.0, 10.0, 1.5) [extrapolation] = {lerp(0.0, 10.0, 1.5)}")


def demo_vectors() -> None:
    print("\n--- [ex02] Vector demonstrations ---")
    u = Vector([2.0, 1.0])
    v = Vector([4.0, 2.0])
    print(f"u ={u}\nv ={v}")
    result = lerp(u, v, 0.3)
    print(f"lerp(u, v, 0.3) ={result}")


def demo_matrices() -> None:
    print("\n--- [ex02] Matrix demonstrations ---")
    u = Matrix([[2.0, 1.0], [3.0, 4.0]])
    v = Matrix([[20.0, 10.0], [30.0, 40.0]])
    print(f"u ={u}\nv ={v}")
    result = lerp(u, v, 0.5)
    print(f"lerp(u, v, 0.5) ={result}")


def demo_errors() -> None:
    print("\n--- [ex02] Error handling demonstrations ---")
    try:
        _ = lerp(1.0, Vector([1.0]), 0.5)  # type: ignore[type-var]
    except TypeError as e:
        print(f"Caught expected type mismatch: {e}")

    try:
        _ = lerp(Vector([1.0]), Vector([1.0, 2.0]), 0.5)
    except ValueError as e:
        print(f"Caught expected dimension mismatch: {e}")


def main() -> None:
    print("========================================")
    print("    Exercise 02: Linear Interpolation   ")
    print("========================================")
    demo_scalars()
    demo_vectors()
    demo_matrices()
    demo_errors()


if __name__ == "__main__":
    main()
