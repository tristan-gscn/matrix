from matrix._core import Vector
from matrix.functions.angle_cos import angle_cos


def demo_subject_examples() -> None:
    print("--- [ex05] Subject examples ---")
    u1 = Vector([1.0, 0.0])
    v1 = Vector([1.0, 0.0])
    print(f"u1 ={u1}\nv1 ={v1}")
    print(f"angle_cos(u1, v1) = {angle_cos(u1, v1)}")

    u2 = Vector([1.0, 0.0])
    v2 = Vector([0.0, 1.0])
    print(f"\nu2 ={u2}\nv2 ={v2}")
    print(f"angle_cos(u2, v2) = {angle_cos(u2, v2)}")

    u3 = Vector([-1.0, 1.0])
    v3 = Vector([1.0, -1.0])
    print(f"\nu3 ={u3}\nv3 ={v3}")
    print(f"angle_cos(u3, v3) = {angle_cos(u3, v3)}")

    u4 = Vector([2.0, 1.0])
    v4 = Vector([4.0, 2.0])
    print(f"\nu4 ={u4}\nv4 ={v4}")
    print(f"angle_cos(u4, v4) = {angle_cos(u4, v4)}")

    u5 = Vector([1.0, 2.0, 3.0])
    v5 = Vector([4.0, 5.0, 6.0])
    print(f"\nu5 ={u5}\nv5 ={v5}")
    print(f"angle_cos(u5, v5) = {angle_cos(u5, v5):.9f}")


def demo_errors() -> None:
    print("\n--- [ex05] Error handling demonstrations ---")
    try:
        u = Vector([1.0, 0.0])
        v = Vector([1.0, 0.0, 0.0])
        _ = angle_cos(u, v)
    except ValueError as e:
        print(f"Caught expected dimension mismatch: {e}")

    try:
        u = Vector([0.0, 0.0])
        v = Vector([1.0, 2.0])
        _ = angle_cos(u, v)
    except ZeroDivisionError as e:
        print(f"Caught expected zero division: {e}")


def main() -> None:
    print("========================================")
    print("          Exercise 05: Cosine           ")
    print("========================================")
    demo_subject_examples()
    demo_errors()


if __name__ == "__main__":
    main()
