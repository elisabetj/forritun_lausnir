from copy import deepcopy

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
    """Returns a full copy of the given list."""

    # For nested lists (or more generally lists that have mutable objects as elements),
    # you want to use deepcopy instead, imported from the copy package (see top):
    complete_copy = deepcopy(int_list)
    return complete_copy


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""

    return [number for number in int_list if number % 2 == 0]
