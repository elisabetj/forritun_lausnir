from typing import List


def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""

    remove_odds_6(int_list)


def remove_odds_6(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Makes a new list with the even numbers only,
    and then modifies the original list to match.
    """

    only_evens = extract_evens(int_list)

    # Copy the correct list into the original, one even number at a time.
    i = 0
    while i < len(only_evens):
        int_list[i] = only_evens[i]
        i += 1

    # And make sure to cut off anything that has not already been overwritten.
    while len(int_list) > len(only_evens):
        int_list.pop()


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""

    return [number for number in int_list if number % 2 == 0]
