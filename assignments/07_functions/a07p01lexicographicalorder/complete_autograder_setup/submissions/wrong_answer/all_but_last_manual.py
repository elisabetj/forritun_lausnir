"""Shows a more realistic way of making the mistake tested for with `all_but_last.py`

See the file `/accepted/manual_loop_while.py` first, for more explanations.
"""


def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order - almost.

    Ignores case.
    """

    length_of_shorter_string = min(len(first), len(second))
    index = 0
    # while index < length_of_shorter_string:
    # or
    # while index <= length_of_shorter_string - 1:
    # both work.
    # This, however, does not work:
    while index < length_of_shorter_string - 1:
        letter_in_first = first[index].lower()
        letter_in_second = second[index].lower()

        if letter_in_first < letter_in_second:
            return first
        elif letter_in_second < letter_in_first:
            return second

        index += 1

    # If we complete the above loop without hitting a return statement,
    # we still haven't compared the last pair of corresponding letters.
    # And the rest of the code below doesn't help with that problem.

    if len(first) < len(second):
        return first

    return second
