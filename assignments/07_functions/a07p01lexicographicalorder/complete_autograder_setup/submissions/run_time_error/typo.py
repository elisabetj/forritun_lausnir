# NOTE: The function name is missing an e so the import will fail
def preceds(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """

    if first.lower() < second.lower():
        return first

    return second
