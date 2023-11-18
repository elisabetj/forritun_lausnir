from typing import Tuple


SIDE_SEPARATOR = "<=>"
FORMULA_SEPARATOR = "+"


def main():
    equation = get_equation()
    left_side, right_side = get_sides(equation)

    chemicals_on_left_side = get_chemicals_in_side(left_side)
    chemicals_on_right_side = get_chemicals_in_side(right_side)

    compare_sides(chemicals_on_left_side, chemicals_on_right_side)


def get_equation() -> str:
    """Asks the user for a chemical equation, and returns it."""

    return input()


def get_sides(equation: str) -> Tuple[str]:
    """Separates and returns the two sides of a given chemical equation."""

    raise NotImplementedError  # TODO: Remove this line and implement the function.


def get_chemicals_in_side(one_side_of_equation: str) -> set:
    """Returns the set of all elements appearing on one side of a chemical equation."""

    raise NotImplementedError  # TODO: Remove this line and implement the function.


def compare_sides(left_set: set, right_set: set) -> None:
    """States the chemicals missing from one side, in alphabetical order, if any."""

    raise NotImplementedError  # TODO: Remove this line and implement the function.


if __name__ == "__main__":
    main()
