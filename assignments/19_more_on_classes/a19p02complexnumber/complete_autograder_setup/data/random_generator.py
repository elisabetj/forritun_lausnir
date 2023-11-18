#!/usr/bin/python3
import random
import sys
from string import ascii_letters

random.seed(sys.argv[-1])

MIN_N = -100
MAX_N = 100

MIN_PARAMS = int(sys.argv[2]) if len(sys.argv) > 3 else 0
MAX_PARAMS = int(sys.argv[3]) if len(sys.argv) > 4 else 2
assert 0 <= MIN_PARAMS <= MAX_PARAMS <= 2, "\n".join(
    [f"Number of parameters: {len(sys.argv)}", f"Parameters: {sys.argv}"]
)
MIN_SECOND = int(sys.argv[4]) if len(sys.argv) > 5 else 0
MAX_SECOND = int(sys.argv[5]) if len(sys.argv) > 6 else 2
assert 0 <= MIN_SECOND <= MAX_SECOND <= 2, "\n".join(
    [f"Number of parameters: {len(sys.argv)}", f"Parameters: {sys.argv}"]
)

test_type = sys.argv[1]

# Inputs needed for each method
# "__init__"   : [re, [im]]
# "__str__"    : C
# "__repr__"   : C
# "re"         : C
# "im"         : C
# "__eq__"     : CxC
# "conjugate"  : C
# "__neg__"    : C
# "__add__"    : CxC
# "__sub__"    : CxC
# "__mul__"    : CxC
# "inverse"    : C
# "__truediv__": CxC


def main():
    print(test_type)

    if test_type in [
        "__init__",
        "__str__",
        "__repr__",
        "re",
        "im",
        "conjugate",
        "__neg__",
        "inverse",
    ]:
        print_complex_number(min_spec=MIN_PARAMS, max_spec=MAX_PARAMS)

    elif test_type in [
        "__eq__",
        "__add__",
        "__sub__",
        "__mul__",
        "__truediv__",
    ]:
        min_for_first, max_for_first = MIN_PARAMS, MAX_PARAMS
        print_complex_number(min_spec=min_for_first, max_spec=max_for_first)
        min_for_second, max_for_second = MIN_SECOND, MAX_SECOND
        print_complex_number(min_spec=min_for_second, max_spec=max_for_second)
    else:
        assert False, f"Unexpected test type: '{test_type}'."


def print_complex_number(min_spec=0, max_spec=2):
    assert 0 <= min_spec <= max_spec <= 2
    re, im = create_complex_number()
    number_of_specified_coordinates = random.randint(min_spec, max_spec)
    print(number_of_specified_coordinates)
    if number_of_specified_coordinates > 0:
        print(f" {re}")
    if number_of_specified_coordinates > 1:
        print(f" {im}")


def create_complex_number():
    # TODO: Consider also using floats,
    # but beware risk of floating point errors when testing `__repr__()`,
    # when tokenizer cannot separate the numbers from surrounding tokens.
    re = random.randint(MIN_N, MAX_N)
    im = random.randint(MIN_N, MAX_N)
    return re, im


if __name__ == "__main__":
    main()
