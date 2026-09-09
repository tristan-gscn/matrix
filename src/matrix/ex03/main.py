from matrix._core import Vector


def demo_subject_examples() -> None:
    print("--- [ex03] Dot product demonstrations ---")
    u1 = Vector([0.0, 0.0])
    v1 = Vector([1.0, 1.0])
    print(f"u1 ={u1}\nv1 ={v1}")
    print(f"u1.dot(v1) = {u1.dot(v1)}")

    u2 = Vector([1.0, 1.0])
    v2 = Vector([1.0, 1.0])
    print(f"\nu2 ={u2}\nv2 ={v2}")
    print(f"u2.dot(v2) = {u2.dot(v2)}")

    u3 = Vector([-1.0, 6.0])
    v3 = Vector([3.0, 2.0])
    print(f"\nu3 ={u3}\nv3 ={v3}")
    print(f"u3.dot(v3) = {u3.dot(v3)}")


def demo_errors() -> None:
    print("\n--- [ex03] Error handling demonstrations ---")
    try:
        u = Vector([1.0, 2.0])
        v = Vector([1.0, 2.0, 3.0])
        _ = u.dot(v)
    except ValueError as e:
        print(f"Caught expected dimension mismatch: {e}")

    try:
        u = Vector([1.0, 2.0])
        _ = u.dot([1.0, 2.0])  # type: ignore[arg-type]
    except TypeError as e:
        print(f"Caught expected type error: {e}")


def main() -> None:
    print("========================================")
    print("        Exercise 03: Dot Product        ")
    print("========================================")
    demo_subject_examples()
    demo_errors()


if __name__ == "__main__":
    main()
