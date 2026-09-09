"""Matrix package: Linear Algebra in Rust with Python bindings."""

import sys
from typing import Callable

from matrix._core import Matrix, Vector
from matrix.functions.linear_combination import linear_combination

__all__ = ["Vector", "Matrix", "linear_combination", "main"]


def _run_ex00() -> None:
    from matrix.mains.ex00 import main as ex00_main
    ex00_main()


def _run_ex01() -> None:
    from matrix.mains.ex01 import main as ex01_main
    ex01_main()


EXERCISES: dict[str, tuple[str, Callable[[], None]]] = {
    "00": ("Exercise 00 - Add, Subtract and Scale", _run_ex00),
    "01": ("Exercise 01 - Linear Combination", _run_ex01),
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
