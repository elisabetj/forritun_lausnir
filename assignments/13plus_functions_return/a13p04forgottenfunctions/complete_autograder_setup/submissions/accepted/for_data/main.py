from importlib import import_module
from pathlib import Path
import sys
import important_library


def sum(a: int, b: int) -> int:
    """
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
    """
    assert False, "Do not call the function!"
    return a + b


def main():
    function_name = input()
    function_info = test_get_function_info(function_name)
    print(function_info)


def test_get_function_info(test_input):
    # Arrange.
    original_input = test_input[:]

    function_name = "get_function_info"
    get_function_info = get_function(function_name)
    expected_return_type = str

    # Act.
    actual = get_function_info(get_function(test_input))

    # Assert.

    assert isinstance(actual, expected_return_type)
    # assert actual == expected_value_afterwards

    return actual


def get_function(name):
    for module in load_modules():
        if hasattr(module, name):
            return getattr(module, name)

    raise NameError(f"Name '{name}' is not defined.")


def load_modules():
    modules = [
        important_library,
        sys.modules[__name__],
    ]  # math, random, threading, collections, builtins, time,
    this_file = Path(__file__)
    for submission_file in this_file.parent.iterdir():
        if submission_file == this_file:
            continue

        if submission_file.suffix == ".py":
            modules.append(import_module(submission_file.stem))

    return modules


if __name__ == "__main__":
    main()
