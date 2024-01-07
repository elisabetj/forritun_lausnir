#!/usr/bin/python3

from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.


def main() -> None:
    """Plays a simple version of Yatzy."""
    dice_list = get_dice_values()
    while dice_list:
        check_value(dice_list)
        dice_list = get_dice_values()


def get_dice_values() -> List[int]:
    """Returns the values of 5 dice, as a list, entered by the user."""
    str_list = input().split()
    num_list = [int(element) for element in str_list]
    return num_list


def check_value(dice_list: List[int]) -> None:
    """Checks and prints out the value of specific dice combinations."""
    count_list = get_counts(dice_list)

    for func in [yatzy, three_of_a_kind, pair]:
        value = check_combination(func, count_list)
        if value != 0:
            return

    print(0)


def get_counts(dice_results: List[int]) -> List[int]:
    """Counts how often each value appears.

    Returns a list of counts
    for each possible outcome on a die roll,
    where the first count in the list
    (at position 0 in the output list)
    indicates how many 1's appear
    in the given list of dice results,
    the second count (at position 1)
    indicates how many 2's appear, and so on.
    The count list is as long as there are sides on the dice.

    For example, if the dice list is [3, 3, 4, 4, 1],
    then the count list is [1, 0, 2, 2, 0, 0],
    indicating that the number 1 appears once,
    the numbers 3 and 4 appear twice each,
    but the numbers 2, 5 and 6 never appear.
    """

    counts = [dice_results.count(value) for value in range(1, MAX_DICE_RESULT + 1)]
    return counts


def check_combination(function: callable, count_list: List[int]) -> int:
    """Checks whether a specific combination of dice occurred
    by calling the supplied function with count_list as parameter.
    Prints the value of the combination if it occurred.
    Returns the value of the combination.
    """
    value = function(count_list)
    if value != 0:
        print(value)
    return value


def yatzy(count_list: List[int]) -> int:
    """Returns 50 if all dice numbers, indicated by count_list,
    are equal, otherwise 0."""
    idx_found = get_highest_index(5, count_list)
    return 50 if idx_found > -1 else 0


def three_of_a_kind(count_list: List[int]) -> int:
    """Returns the value of the three of a kind,
    indicated by count_list, or 0 if no triple is found."""
    idx_found = get_highest_index(3, count_list)
    return 3 * (idx_found + 1) if idx_found > -1 else 0


def pair(count_list: List[int]) -> int:
    """Returns the value of the highest pair,
    indicated by count_list, or 0 if no pair found."""
    idx_found = get_highest_index(2, count_list)
    return 2 * (idx_found + 1) if idx_found > -1 else 0


def get_highest_index(number: int, a_list: List[int]) -> int:
    """Returns the highest index for a value >= number in a_list,
    or 0 if such a value does not exist.

    Example: get_highest_index(2, [1, 0, 2, 3, 0]) = 3.
    """
    idx_found = -1
    for i in range(len(a_list)):
        if a_list[i] >= number:
            idx_found = i

    return idx_found


if __name__ == "__main__":
    main()
