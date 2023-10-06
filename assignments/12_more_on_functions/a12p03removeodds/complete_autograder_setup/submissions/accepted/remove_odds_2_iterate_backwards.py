from typing import List


def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""

    remove_odds_2(int_list)


def remove_odds_2(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Iterates backwards over the list, so it can safely modify the list on the fly.
    """

    for num in int_list[::-1]:
        if num % 2 == 1:
            int_list.remove(num)

    # Here, if we remove an element from the list,
    # it doesn't affect the index of any elements that remain to be seen,
    # because they are all further left.
    #
    # And in case the same number appears more than once,
    # then we'll remove the first occurrence instead,
    # but that's all right, because then the occurrence we just saw
    # will move one seat to the left also,
    # so we'll see it again immediately in the next step,
    # and try to remove it again.
    # This is repeated until it becomes the last occurence of the number,
    # and then it will itself be removed,
    # and we continue on to the next number to the left.


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""

    return [number for number in int_list if number % 2 == 0]
