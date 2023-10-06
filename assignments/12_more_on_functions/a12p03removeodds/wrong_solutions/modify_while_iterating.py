from typing import List


def remove_odds(int_list: List[int]) -> None:
    """Attempts to remove odd integers from the given list."""

    remove_odds_1(int_list)


def remove_odds_1(int_list: List[int]) -> None:
    """Attempts to remove odd integers from the given list."""

    # If we iterate over int_list itself,
    # and also modify int_list while we are iterating over it, like this:
    for num in int_list:
        if num % 2 == 1:
            int_list.remove(num)
    # then we run into problems, because if we remove a number from the list,
    # then the rest of the list will move one seat to the left.
    # But the index also moves one seat to the right,
    # and thus will skip over the next element in the list.
    # That's no good.


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""

    return [number for number in int_list if number % 2 == 0]
