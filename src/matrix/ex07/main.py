from matrix import Matrix, Vector


def demo_mul_vec() -> None:
    print("--- [ex07] Matrix-Vector multiplication (mul_vec & *) ---")
    u1 = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v1 = Vector([4.0, 2.0])
    print(f"u1 ={u1}\nv1 ={v1}")
    print(f"u1.mul_vec(v1) ={u1.mul_vec(v1)}")
    print(f"u1 * v1 ={u1 * v1}")

    u2 = Matrix([[2.0, 0.0], [0.0, 2.0]])
    print(f"\nu2 ={u2}\nv1 ={v1}")
    print(f"u2.mul_vec(v1) ={u2.mul_vec(v1)}")

    u3 = Matrix([[2.0, -2.0], [-2.0, 2.0]])
    print(f"\nu3 ={u3}\nv1 ={v1}")
    print(f"u3.mul_vec(v1) ={u3.mul_vec(v1)}")


def demo_mul_mat() -> None:
    print("\n--- [ex07] Matrix-Matrix multiplication (mul_mat & *) ---")
    identity = Matrix([[1.0, 0.0], [0.0, 1.0]])
    print(f"I ={identity}")
    print(f"I.mul_mat(I) ={identity.mul_mat(identity)}")

    m1 = Matrix([[2.0, 1.0], [4.0, 2.0]])
    print(f"\nI * m1 ={identity * m1}")

    m2 = Matrix([[3.0, -5.0], [6.0, 8.0]])
    print(f"\nm2 ={m2}\nm1 ={m1}")
    print(f"m2.mul_mat(m1) ={m2.mul_mat(m1)}")
    print(f"m2 * m1 ={m2 * m1}")


def demo_errors() -> None:
    print("\n--- [ex07] Error handling demonstrations ---")
    try:
        m = Matrix([[1.0, 2.0], [3.0, 4.0]])
        v = Vector([1.0, 2.0, 3.0])
        _ = m.mul_vec(v)
    except ValueError as e:
        print(f"Caught expected mul_vec dimension mismatch: {e}")

    try:
        a = Matrix([[1.0, 2.0], [3.0, 4.0]])  # 2x2
        b = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])  # 3x2
        _ = a.mul_mat(b)
    except ValueError as e:
        print(f"Caught expected mul_mat dimension mismatch: {e}")


def main() -> None:
    print("========================================")
    print("  Exercise 07: Linear map, Matrix mul   ")
    print("========================================")
    demo_mul_vec()
    demo_mul_mat()
    demo_errors()


if __name__ == "__main__":
    main()
