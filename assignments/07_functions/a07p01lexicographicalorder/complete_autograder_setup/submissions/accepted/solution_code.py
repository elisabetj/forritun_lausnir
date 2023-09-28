def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """

    if first.lower() < second.lower():  # Compare in lower case...
        return first  # but return the original.

    return second


if __name__ == "__main__":
    print(precedes(input(), input()))
