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

    return equation.split(SIDE_SEPARATOR)


def get_chemicals_in_side(one_side_of_equation: str) -> set:
    """Returns the set of all elements appearing on one side of a chemical equation."""

    formulae = one_side_of_equation.split(FORMULA_SEPARATOR)
    
    overall_set = set()
    for formula in formulae:
        chemical_set = get_chemicals_in_formula(formula.strip())
        overall_set.update(chemical_set)

    return overall_set


def get_chemicals_in_formula(chemical_formula: str) -> set:
    """Returns the set of element found in the formula."""

    chemical_set = set()
    while chemical_formula:
        if chemical_formula[0].isalpha():
            assert chemical_formula[0].isupper()
            element, chemical_formula = extract_next_element(chemical_formula)
            chemical_set.add(element)
        else:
            assert chemical_formula[0].isdigit()
            ratio_number, chemical_formula = extract_ratio_number(chemical_formula)

    return chemical_set


def extract_next_element(chemical_formula: str) -> Tuple[str]:
    """Parses the next element from the front of the string.

    Assumes it will not be called unless the next character in the chemical formula is an upper case letter.
    Returns the element, as well as the string with the element removed from the front.
    """

    assert chemical_formula and chemical_formula[0].isupper()

    if len(chemical_formula) > 1 and chemical_formula[1].islower():
        symbols = 2
    else:
        symbols = 1

    element = chemical_formula[:symbols]
    rest_of_formula = chemical_formula[symbols:]

    return element, rest_of_formula


def extract_ratio_number(chemical_formula: str) -> tuple:
    """Parses the integer (possibly multiple digits) from the front of the string.

    Returns the integer, if any, otherwise 1, as well as the string with the integer removed.
    """

    ratio_number_str = ""
    while chemical_formula and chemical_formula[0].isdigit():
        ratio_number_str += chemical_formula[0]
        chemical_formula = chemical_formula[1:]

    ratio_number = 1
    if ratio_number_str:
        ratio_number = int(ratio_number_str)

    return ratio_number, chemical_formula


def compare_sides(left_set: set, right_set: set) -> None:
    """States the chemicals missing from one side, in alphabetical order, if any."""

    if left_set == right_set:
        print("No elements missing from either side of the equation.")
    else:
        missing_from_right_side = left_set - right_set
        if missing_from_right_side:
            print(f"The following elements appear on the left side but not the right:")
            print(", ".join(sorted(missing_from_right_side)))

        missing_from_left_side = right_set - left_set
        if missing_from_left_side:
            print(f"The following elements appear on the right side but not the left:")
            print(", ".join(sorted(missing_from_left_side)))

        print("Therefore, balancing this chemical equation is not possible.")


if __name__ == "__main__":
    main()
