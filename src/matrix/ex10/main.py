from matrix import Matrix


def demo_subject_examples() -> None:
    print("--- [ex10] Subject examples ---")
    u1 = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    print(f"u1 (identity) ={u1}")
    print(f"u1.row_echelon() ={u1.row_echelon()}")

    u2 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    print(f"\nu2 ={u2}")
    print(f"u2.row_echelon() ={u2.row_echelon()}")

    u3 = Matrix([[1.0, 2.0], [2.0, 4.0]])
    print(f"\nu3 (linearly dependent) ={u3}")
    print(f"u3.row_echelon() ={u3.row_echelon()}")

    u4 = Matrix(
        [
            [8.0, 5.0, -2.0, 4.0, 28.0],
            [4.0, 2.5, 20.0, 4.0, -4.0],
            [8.0, 5.0, 1.0, 4.0, 17.0],
        ]
    )
    print(f"\nu4 (3x5 rectangular) ={u4}")
    print(f"u4.row_echelon() ={u4.row_echelon()}")


def demo_edge_cases() -> None:
    print("\n--- [ex10] Special & edge cases ---")
    zeros = Matrix([[0.0, 0.0], [0.0, 0.0]])
    print(f"Zero matrix ={zeros}")
    print(f"zeros.row_echelon() ={zeros.row_echelon()}")

    tall = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    print(f"\nTall matrix (3x2) ={tall}")
    print(f"tall.row_echelon() ={tall.row_echelon()}")


def main() -> None:
    print("========================================")
    print("     Exercise 10: Row-Echelon Form      ")
    print("========================================")
    demo_subject_examples()
    demo_edge_cases()


if __name__ == "__main__":
    main()
