def precedes(first: str, second: str) -> str:
    """Returns the shorter string, instead of comparing lexicographical order as it is supposed to."""

    if len(first.lower()) < len(second.lower()):
        return first

    return second
