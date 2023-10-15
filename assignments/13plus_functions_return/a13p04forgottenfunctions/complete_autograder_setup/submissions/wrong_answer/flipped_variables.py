from importlib import import_module
from pathlib import Path
import sys


def important_funcrion1() -> str:
    """
    impottant_function1

    returns the string "False"
    """
    return "False"


def new_line(i: int) -> int:
    """
    new_line(i: int) -> int

    input i

    output "\n" times i

    so for example i = 4
    rturn "\n\n\n\n"
    """
    return "\n" * i


def tan() -> None:
    """
    Return the tangent of x (measured in radians).
    """
    assert False, "Do not call the function!"
    return


def sleep() -> None:
    """
    sleep(seconds)

    Delay execution for a given number of seconds.  The argument may be
    a floating point number for subsecond precision.
    """
    assert False, "Do not call the function!"
    return


def randint() -> None:
    """
    Return random integer in range [a, b], including both end points.
    """
    assert False, "Do not call the function!"
    return


def enumerate() -> None:
    """
    Return a list of all Thread objects currently alive.

        The list includes daemonic threads, dummy thread objects created by
        current_thread(), and the main thread. It excludes terminated threads and
        threads that have not yet been started.
    """
    assert False, "Do not call the function!"
    return


def namedtuple() -> None:
    """
    Returns a new subclass of tuple with named fields.

        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    assert False, "Do not call the function!"
    return


def cos() -> None:
    """
    Return the cosine of x (measured in radians).
    """
    assert False, "Do not call the function!"
    return


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


def get_function_info(function: callable) -> str:
    divider = "-" * 40
    return f"Name: {function.__doc__}\n{divider}\n{function.__name__}"


def test_get_function_info(test_input):
    # Arrange.
    # original_input = test_input[:]

    # function_name = "get_function_info"
    # get_function_info = get_function(function_name)
    expected_return_type = str
    # expected_value_afterwards =

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
    modules = [sys.modules[__name__]]
    this_file = Path(__file__)
    for submission_file in this_file.parent.iterdir():
        if submission_file == this_file:
            continue

        if submission_file.suffix == ".py":
            modules.append(import_module(submission_file.stem))

    return modules


if __name__ == "__main__":
    main()
