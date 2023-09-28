def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """

    if first.lower() < second.lower():
        return first

    return second
