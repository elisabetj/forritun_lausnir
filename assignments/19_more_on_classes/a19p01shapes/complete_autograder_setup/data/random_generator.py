#!/usr/bin/python3
import random
import sys
from string import ascii_letters

random.seed(sys.argv[-1])

MIN_N = 1
MAX_N = 100

# Inputs needed for each class
# "Rectangle" : NxN
# "Square" : N

RECTANGLE = "Rectangle"
SQUARE = "Square"
METHODS = [
    "__init__",
    "__str__",
    "get_perimeter",
    "get_area",
]

class_to_test = sys.argv[1]
method_to_test = sys.argv[2]
assert class_to_test in [
    RECTANGLE,
    SQUARE,
], f"Unexpected class {class_to_test} requested."
assert method_to_test in METHODS, f"Unexpected method {method_to_test} requested."


def main():
    print(f"{class_to_test}.{method_to_test}")

    if class_to_test == RECTANGLE:
        print_rectangle()
    elif class_to_test == SQUARE:
        print_square()
    else:
        assert False, f"Unexpected test type: '{class_to_test}.{method_to_test}'."


def print_rectangle():
    # TODO: Consider also using floats.
    width = random.randint(MIN_N, MAX_N)
    height = random.randint(MIN_N, MAX_N)
    print(f"{width}, {height}")


def print_square():
    # TODO: Consider also using floats.
    side = random.randint(MIN_N, MAX_N)
    print(side)


if __name__ == "__main__":
    main()
