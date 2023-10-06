from typing import List


def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""

    remove_odds_5(int_list)


def remove_odds_5(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Takes care not to move on to the next index
    at the same time as the rest of the list is moved backwards
    (thus skipping over one element).
    """

    i = 0
    while i < len(int_list):
        if int_list[i] % 2 == 1:
            int_list.pop(i)
        else:
            i += 1


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""

    return [number for number in int_list if number % 2 == 0]
