from typing import List


def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""

    remove_odds_8(int_list)


def remove_odds_8(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Makes a new list with the even numbers only,
    and then modifies the original list to match.
    """

    only_evens = extract_evens(int_list)

    # Simply replace all the contents of the original list with the new one.
    int_list[:] = only_evens


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""

    return [number for number in int_list if number % 2 == 0]
