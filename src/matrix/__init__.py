"""Matrix package: Linear Algebra in Rust with Python bindings."""

import sys
from typing import Callable

from matrix._core import Matrix, Vector
from matrix.ex01.linear_combination import linear_combination
from matrix.ex02.lerp import lerp
from matrix.ex05.angle_cos import angle_cos
from matrix.ex06.cross_product import cross_product

__all__ = [
    "Vector",
    "Matrix",
    "linear_combination",
    "lerp",
    "angle_cos",
    "cross_product",
    "main",
]


def _run_ex00() -> None:
    from matrix.ex00.main import main as ex00_main
    ex00_main()


def _run_ex01() -> None:
    from matrix.ex01.main import main as ex01_main
    ex01_main()


def _run_ex02() -> None:
    from matrix.ex02.main import main as ex02_main
    ex02_main()


def _run_ex03() -> None:
    from matrix.ex03.main import main as ex03_main
    ex03_main()


def _run_ex04() -> None:
    from matrix.ex04.main import main as ex04_main
    ex04_main()


def _run_ex05() -> None:
    from matrix.ex05.main import main as ex05_main
    ex05_main()


def _run_ex06() -> None:
    from matrix.ex06.main import main as ex06_main
    ex06_main()


def _run_ex07() -> None:
    from matrix.ex07.main import main as ex07_main
    ex07_main()


def _run_ex08() -> None:
    from matrix.ex08.main import main as ex08_main
    ex08_main()


def _run_ex09() -> None:
    from matrix.ex09.main import main as ex09_main
    ex09_main()


def _run_ex10() -> None:
    from matrix.ex10.main import main as ex10_main
    ex10_main()


def _run_ex11() -> None:
    from matrix.ex11.main import main as ex11_main
    ex11_main()


EXERCISES: dict[str, tuple[str, Callable[[], None]]] = {
    "00": ("Exercise 00 - Add, Subtract and Scale", _run_ex00),
    "01": ("Exercise 01 - Linear Combination", _run_ex01),
    "02": ("Exercise 02 - Linear Interpolation", _run_ex02),
    "03": ("Exercise 03 - Dot Product", _run_ex03),
    "04": ("Exercise 04 - Norm", _run_ex04),
    "05": ("Exercise 05 - Cosine", _run_ex05),
    "06": ("Exercise 06 - Cross Product", _run_ex06),
    "07": ("Exercise 07 - Linear map, Matrix multiplication", _run_ex07),
    "08": ("Exercise 08 - Trace", _run_ex08),
    "09": ("Exercise 09 - Transpose", _run_ex09),
    "10": ("Exercise 10 - Row-Echelon Form", _run_ex10),
    "11": ("Exercise 11 - Determinant", _run_ex11),
}


def _print_help() -> None:
    print("Usage:")
    print("  make run ARGS=<exercise>    Run an exercise (e.g. ARGS=00)")
    print("  make run ARGS=all           Run all available exercises\n")
    print("Available exercises:")
    for key, (desc, _) in EXERCISES.items():
        print(f"  ex{key} : {desc}")


def main() -> None:
    """Entrypoint for `matrix` CLI and `make run`."""
    args = sys.argv[1:]

    if not args or args[0].lower() in ("-h", "--help", "help"):
        _print_help()
        return

    target = args[0].lower().removeprefix("ex")

    if target in ("all", "--all"):
        for _, (_, runner) in EXERCISES.items():
            runner()
            print()
        return

    if target in EXERCISES:
        _, runner = EXERCISES[target]
        runner()
    else:
        print(f"Unknown exercise: '{args[0]}'\n")
        _print_help()
        sys.exit(1)
