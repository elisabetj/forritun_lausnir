def sum(a: int, b: int) -> int:
    """
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
    """
    assert False, "Do not call the function!"
    return a + b


def important_function1() -> str:
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
