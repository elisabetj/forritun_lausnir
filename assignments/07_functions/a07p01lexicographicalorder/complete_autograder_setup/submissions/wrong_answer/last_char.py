def precedes(first: str, second: str) -> str:
    """Returns the string whose last letter comes first in lexicographical order.

    Ignores case.
    Also ignores all letters except the last one in each string.
    And fails in case either string is empty.
    """

    if first.lower()[-1] < second.lower()[-1]:
        return first

    return second
