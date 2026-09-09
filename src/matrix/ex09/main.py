from matrix import Matrix


def demo_rectangles() -> None:
    print("--- [ex09] Rectangular matrix transpose ---")
    m1 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    print(f"A (2x3) ={m1}")
    print(f"A.transpose() (3x2) ={m1.transpose()}")

    m2 = Matrix([[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]])
    print(f"\nB (3x2) ={m2}")
    print(f"B.transpose() (2x3) ={m2.transpose()}")


def demo_square_and_vectors() -> None:
    print("\n--- [ex09] Square and row/column matrices ---")
    sq = Matrix([[1.0, 2.0], [3.0, 4.0]])
    print(f"Square ={sq}")
    print(f"Square.transpose() ={sq.transpose()}")

    row_mat = Matrix([[1.0, 2.0, 3.0]])
    print(f"\nRow matrix (1x3) ={row_mat}")
    print(f"Row matrix.transpose() (3x1) ={row_mat.transpose()}")


def demo_properties() -> None:
    print("\n--- [ex09] Algebraic properties of transposition ---")
    a = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = Matrix([[7.0, 8.0], [9.0, 1.0], [2.0, 3.0]])

    print(f"(A^T)^T == A: {a.transpose().transpose() == a}")
    prod_t = (a * b).transpose()
    rev_prod = b.transpose() * a.transpose()
    print(f"(A * B)^T == B^T * A^T: {prod_t == rev_prod}")


def main() -> None:
    print("========================================")
    print("         Exercise 09: Transpose         ")
    print("========================================")
    demo_rectangles()
    demo_square_and_vectors()
    demo_properties()


if __name__ == "__main__":
    main()
