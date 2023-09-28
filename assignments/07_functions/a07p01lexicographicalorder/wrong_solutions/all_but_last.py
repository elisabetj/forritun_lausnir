def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order - almost.

    Ignores case.
    """

    if first.lower()[:-1] < second.lower()[:-1]:
        return first

    return second
