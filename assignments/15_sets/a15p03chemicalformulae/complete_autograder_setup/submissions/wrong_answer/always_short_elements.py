from typing import Tuple


def main():
    formula_1, formula_2 = get_formulae()

    chemical_set_1 = get_chemicals_in_formula(formula_1)
    chemical_set_2 = get_chemicals_in_formula(formula_2)

    state_common_chemicals(chemical_set_1, chemical_set_2)


def get_formulae() -> Tuple[str, str]:

    formula_1 = input()
    formula_2 = input()

    return formula_1, formula_2


def get_chemicals_in_formula(chemical_formula: str) -> set:

    chemical_set = set()
    while chemical_formula:
        if chemical_formula[0].isalpha() and chemical_formula[0].isupper():
            element, chemical_formula = extract_next_element(chemical_formula)
            chemical_set.add(element)
        else:
            chemical_formula = chemical_formula[1:]
    return chemical_set


def extract_next_element(chemical_formula: str) -> Tuple[str, str]:

    element = chemical_formula[:1]
    rest_of_formula = chemical_formula[1:]

    return element, rest_of_formula

def state_common_chemicals(chemical_set_1: set, chemical_set_2: set) -> None:

    common_chemicals = chemical_set_1.intersection(chemical_set_2)
    print(", ".join(sorted(common_chemicals)))


if __name__ == "__main__":
    main()
