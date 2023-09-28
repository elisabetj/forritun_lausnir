"""Same as `manual_loop_for.py` except with a while loop instead of a for loop.

See the other file first, for more explanations.
"""


def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """

    length_of_shorter_string = min(len(first), len(second))
    index = 0
    # while index <= length_of_shorter_string - 1:
    # also works, but let's stick with the shorter version:
    while index < length_of_shorter_string:
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
