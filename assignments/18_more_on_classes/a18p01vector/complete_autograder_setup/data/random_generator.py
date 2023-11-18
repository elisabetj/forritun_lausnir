#!/usr/bin/python3
import random
import sys


random.seed(sys.argv[-1])

MIN_N = -100
MAX_N = 100

MIN_PARAMS = int(sys.argv[2]) if len(sys.argv) > 3 else 0
MAX_PARAMS = int(sys.argv[3]) if len(sys.argv) > 4 else 3
assert 0 <= MIN_PARAMS <= MAX_PARAMS <= 3, "\n".join(
    [f"Number_of_parameters: {len(sys.argv)}", f"Parameters: {sys.argv}"]
)
MIN_SECOND = int(sys.argv[4]) if len(sys.argv) > 5 else 0
MAX_SECOND = int(sys.argv[5]) if len(sys.argv) > 6 else 3
assert 0 <= MIN_SECOND <= MAX_SECOND <= 3, "\n".join(
    [f"Number_of_parameters: {len(sys.argv)}", f"Parameters: {sys.argv}"]
)

test_type = sys.argv[1]


def main():
    print(test_type)

    if test_type in [
        "__init__",
        "__str__",
        "__abs__",
        "__repr__",
    ]:
        print_vector(min_spec=MIN_PARAMS, max_spec=MAX_PARAMS)

    elif test_type in [
        "__mul__",
        "__rmul__",
    ]:
        print_vector(min_spec=MIN_PARAMS, max_spec=MAX_PARAMS)
        scalar = random.randint(MIN_N, MAX_N)
        print(scalar)
    elif test_type in [
        "__add__",
        "__sub__",
        "__eq__",
        "__gt__",
        "__ge__",
        "__lt__",
        "__le__",
        "dot",
        "cross",
    ]:
        min_for_first, max_for_first = MIN_PARAMS, MAX_PARAMS
        print_vector(min_spec=min_for_first, max_spec=max_for_first)
        min_for_second, max_for_second = MIN_SECOND, MAX_SECOND
        print_vector(min_spec=min_for_second, max_spec=max_for_second)
    else:
        assert False, f"Unexpected test type: '{test_type}'."


def print_vector(min_spec=0, max_spec=3):
    x, y, z = create_vector()
    number_of_specified_coordinates = random.randint(min_spec, max_spec)
    print(number_of_specified_coordinates)
    if number_of_specified_coordinates > 0:
        print(x)
    if number_of_specified_coordinates > 1:
        print(y)
    if number_of_specified_coordinates > 2:
        print(z)


def create_vector():
    # TODO: Consider also using floats,
    # but beware risk of floating point errors when testing `__repr__()`,
    # when tokenizer cannot separate the numbers from surrounding tokens.
    x = random.randint(MIN_N, MAX_N)
    y = random.randint(MIN_N, MAX_N)
    z = random.randint(MIN_N, MAX_N)
    return x, y, z


if __name__ == "__main__":
    main()
