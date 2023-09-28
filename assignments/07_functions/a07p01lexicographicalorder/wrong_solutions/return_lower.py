def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order, in lower case.

    Ignores case.
    """

    # Forgets the case of the original strings,
    # overwriting them with their lower-case counterparts.
    first = first.lower()
    second = second.lower()
    if first < second:  # Compare in lower case...
        return first  # and also return lower case!

    return second
