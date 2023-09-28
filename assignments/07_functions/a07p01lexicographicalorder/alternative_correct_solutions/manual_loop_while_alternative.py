"""Same as `manual_loop_for.py` except with a while loop instead of a for loop.

See the other file first, for more explanations.
"""


def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """

    index = 0
    while index < len(first) and index < len(second):
        # Take care not to index out of bounds of either string.
        letter_in_first = first[index].lower()
        letter_in_second = second[index].lower()

        if letter_in_first < letter_in_second:
            return first
        elif letter_in_second < letter_in_first:
            return second

        index += 1

    if len(first) < len(second):
        return first

    return second
