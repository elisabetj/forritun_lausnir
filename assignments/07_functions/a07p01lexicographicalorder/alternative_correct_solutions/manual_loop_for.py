def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """

    # This can also be solved by going through the strings manually,
    # and comparing the corresponding letters.
    # This is basically what the builtin string comparison of Python does.
    # Usually, we want to avail ourselves of already implemented code,
    # so we prefer to use the builtin method (it is tried and tested),
    # but an illustration can be enlightening.
    length_of_shorter_string = min(len(first), len(second))
    for index in range(length_of_shorter_string):
        # Take care not to index out of bounds.
        # As long as we stick within the length of the shorter string,
        # then we can be sure to be within the length of both strings.
        letter_in_first = first[index].lower()
        letter_in_second = second[index].lower()

        # As soon as we see the strings diverge, we know which one comes first.
        if letter_in_first < letter_in_second:  # Compare in lower case...
            return first  # but return the original.
        elif letter_in_second < letter_in_first:
            return second

        # If neither letter is larger than the other, then they're equal,
        # and so we go on to the next index to check the next pair.

    # If we complete the loop above without hitting a return statement,
    # it means that the parts of the strings that we have already compared
    # are equal so far (ignoring case).
    # Then, either the strings are the same, or one is a prefix of the other,
    # meaning the longer string begins with the shorter string.
    # So all we have left to do is to check if they're the same length,
    # and return the shorter one.
    # If they're the same string, it doesn't matter which one we return - kind of.
    # Only thing is, that we're ignoring case in the comparison, but returning the original,
    # so the output might differ in case.
    # In that instance, we return the second one, to conform to the given solution.

    if len(first) < len(second):
        return first

    return second
