def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order.

    Does not ignore case, as it is supposed to.
    """

    if first < second:
        return first

    return second
