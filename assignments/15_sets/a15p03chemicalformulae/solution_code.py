from typing import Tuple


def main():
    formula_1, formula_2 = get_formulae()

    chemical_set_1 = get_chemicals_in_formula(formula_1)
    chemical_set_2 = get_chemicals_in_formula(formula_2)

    state_common_chemicals(chemical_set_1, chemical_set_2)


def get_formulae() -> Tuple[str, str]:
    """Asks the user for two chemical formulae, and returns them."""

    formula_1 = input()
    formula_2 = input()

    return formula_1, formula_2


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


def extract_next_element(chemical_formula: str) -> Tuple[str, str]:
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


def extract_ratio_number(chemical_formula: str) -> Tuple[int, str]:
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


def state_common_chemicals(chemical_set_1: set, chemical_set_2: set) -> None:
    """Prints the chemicals common to both sets, in alphabetical order."""

    common_chemicals = chemical_set_1.intersection(chemical_set_2)
    print(", ".join(sorted(common_chemicals)))


if __name__ == "__main__":
    main()
