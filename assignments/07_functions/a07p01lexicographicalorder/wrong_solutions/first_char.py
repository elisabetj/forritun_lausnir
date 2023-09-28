def precedes(first: str, second: str) -> str:
    """Returns the string whose first letter comes first in lexicographical order.

    Ignores case.
    Also ignores all letters after the first one in each string.
    And fails in case either string is empty.
    """

    if first.lower()[0] < second.lower()[0]:
        return first

    return second
