from typing import List


def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""

    remove_odds_1(int_list)


def remove_odds_1(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Makes a copy first, for reference.
    Iterates over the reference, and modifies the original.
    """

    a_copy = make_a_copy(int_list)

    # We use the copy as a reference that stays unchanged while we iterate over it.
    for num in a_copy:
        if num % 2 == 1:
            int_list.remove(num)


def make_a_copy(int_list: List[int]) -> List[int]:
    """Returns a copy of the given list.

    Demonstrates various ways to copy lists.
    """

    # There are various ways to make a copy. The following all work
    a_copy = int_list[:]
    a_copy = [num for num in int_list]
    a_copy = int_list.copy()
    a_copy = list(int_list)

    # You can also use the copy package.
    # Normally we want to keep imports at the top of the file,
    # but this is just for demonstration purposes,
    # so we keep it here within easy reach.
    from copy import copy

    a_copy = copy(int_list)

    # These all make only shallow copies though,
    # which works fine when the lists are not nested,
    # such as lists of integers, like in this case.

    # For nested lists (or more generally lists that have mutable objects as elements),
    # you want to use deepcopy instead:
    from copy import deepcopy

    complete_copy = deepcopy(int_list)

    # This way does not work:
    not_a_copy = int_list
    # If we modify not_a_copy, then we also modify int_list.
    # And vice versa.

    return a_copy


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""

    return [number for number in int_list if number % 2 == 0]
