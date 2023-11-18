#!/usr/bin/python3
import random
import sys

from string import ascii_lowercase, digits

random.seed(sys.argv[-1])


def main():
    min_elements = int(sys.argv[1])
    max_elements = int(sys.argv[2])

    element_amount = random.randint(min_elements, max_elements)

    formula1 = construct_formula(element_amount)
    formula2 = construct_formula(element_amount)

    print(formula1)
    print(formula2)


def construct_formula(element_amount):
    formula_str = ""
    for _ in range(element_amount):
        formula_str += random_element()
        # TODO: Add numbers as well.
    return formula_str


def random_element():
    length = random.randint(1, 2)
    element = "".join(random.choices(ascii_lowercase, k=length))
    element += "".join(random.choices(digits, k=random.randint(0, 2)))
    return element.capitalize()


if __name__ == "__main__":
    main()
