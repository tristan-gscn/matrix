from matrix import Matrix


def demo_subject_examples() -> None:
    print("--- [ex13] Subject examples ---")
    u1 = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    print(f"u1 ={u1}")
    print(f"u1.rank() = {u1.rank()}")

    u2 = Matrix(
        [
            [1.0, 2.0, 0.0, 0.0],
            [2.0, 4.0, 0.0, 0.0],
            [-1.0, 2.0, 1.0, 1.0],
        ]
    )
    print(f"\nu2 ={u2}")
    print(f"u2.rank() = {u2.rank()}")

    u3 = Matrix(
        [
            [8.0, 5.0, -2.0],
            [4.0, 7.0, 20.0],
            [7.0, 6.0, 1.0],
            [21.0, 18.0, 7.0],
        ]
    )
    print(f"\nu3 ={u3}")
    print(f"u3.rank() = {u3.rank()}")


def demo_edge_cases() -> None:
    print("\n--- [ex13] Special cases ---")
    zeros = Matrix([[0.0, 0.0], [0.0, 0.0]])
    print(f"Zero matrix ={zeros}")
    print(f"zeros.rank() = {zeros.rank()}")

    singular = Matrix([[1.0, 2.0], [2.0, 4.0]])
    print(f"\nSingular matrix ={singular}")
    print(f"singular.rank() = {singular.rank()}")


def main() -> None:
    print("========================================")
    print("            Exercise 13: Rank           ")
    print("========================================")
    demo_subject_examples()
    demo_edge_cases()


if __name__ == "__main__":
    main()
