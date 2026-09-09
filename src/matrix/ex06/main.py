from matrix._core import Vector
from matrix.ex06.cross_product import cross_product


def demo_subject_examples() -> None:
    print("--- [ex06] Subject examples ---")
    u1 = Vector([0.0, 0.0, 1.0])
    v1 = Vector([1.0, 0.0, 0.0])
    print(f"u1 ={u1}\nv1 ={v1}")
    print(f"cross_product(u1, v1) ={cross_product(u1, v1)}")

    u2 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([4.0, 5.0, 6.0])
    print(f"\nu2 ={u2}\nv2 ={v2}")
    print(f"cross_product(u2, v2) ={cross_product(u2, v2)}")

    u3 = Vector([4.0, 2.0, -3.0])
    v3 = Vector([-2.0, -5.0, 16.0])
    print(f"\nu3 ={u3}\nv3 ={v3}")
    print(f"cross_product(u3, v3) ={cross_product(u3, v3)}")


def demo_errors() -> None:
    print("\n--- [ex06] Error handling demonstrations ---")
    try:
        u = Vector([1.0, 2.0])
        v = Vector([3.0, 4.0])
        _ = cross_product(u, v)
    except ValueError as e:
        print(f"Caught expected 2D dimension error: {e}")

    try:
        u = Vector([1.0, 2.0, 3.0, 4.0])
        v = Vector([1.0, 2.0, 3.0, 4.0])
        _ = cross_product(u, v)
    except ValueError as e:
        print(f"Caught expected 4D dimension error: {e}")


def main() -> None:
    print("========================================")
    print("       Exercise 06: Cross Product       ")
    print("========================================")
    demo_subject_examples()
    demo_errors()


if __name__ == "__main__":
    main()
