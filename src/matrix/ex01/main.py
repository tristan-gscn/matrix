"""Exercise 01 - Linear combination."""

from matrix._core import Vector
from matrix.ex01.linear_combination import linear_combination


def demo_subject_examples() -> None:
    print("--- [ex01] Standard basis combination ---")
    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])
    coefs1 = [10.0, -2.0, 0.5]
    print(f"e1 ={e1}\ne2 ={e2}\ne3 ={e3}")
    print(f"coefs = {coefs1}")
    result1 = linear_combination([e1, e2, e3], coefs1)
    print(f"linear_combination([e1, e2, e3], coefs) ={result1}")

    print("\n--- [ex01] General vectors combination ---")
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([0.0, 10.0, -100.0])
    coefs2 = [10.0, -2.0]
    print(f"v1 ={v1}\nv2 ={v2}")
    print(f"coefs = {coefs2}")
    result2 = linear_combination([v1, v2], coefs2)
    print(f"linear_combination([v1, v2], coefs) ={result2}")


def demo_errors() -> None:
    print("\n--- [ex01] Error handling demonstrations ---")
    try:
        v1 = Vector([1.0, 2.0])
        linear_combination([v1], [1.0, 2.0])
    except ValueError as e:
        print(f"Caught expected count mismatch: {e}")

    try:
        v1 = Vector([1.0, 2.0])
        v2 = Vector([1.0, 2.0, 3.0])
        linear_combination([v1, v2], [1.0, 1.0])
    except ValueError as e:
        print(f"Caught expected dimension mismatch: {e}")


def main() -> None:
    print("========================================")
    print("    Exercise 01: Linear Combination     ")
    print("========================================")
    demo_subject_examples()
    demo_errors()


if __name__ == "__main__":
    main()
