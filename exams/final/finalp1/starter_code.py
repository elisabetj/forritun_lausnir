from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.


def main():
    pass


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


if __name__ == "__main__":
    main()
