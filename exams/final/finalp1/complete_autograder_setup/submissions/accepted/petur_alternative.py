#!/usr/bin/python3

from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.
NUMBER_OF_DICE = 5
YATZY = 50


def main():
    """Print simplified yatzy score for a sequence of dice rolls."""
    while line := input():
        dice_values = get_numbers(line)
        counts = get_counts(dice_values)
        print(calculate_score(counts))


def get_numbers(line: str) -> List[int]:
    """Parse a line containing dice results into a list of integers."""
    dice_values = [int(value) for value in line.split()]
    assert len(dice_values) == NUMBER_OF_DICE
    return dice_values


def get_counts(dice_results: List[int]) -> List[int]:
    """Count how often each value appears.

    Return a list of counts
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

    assert len(dice_results) == NUMBER_OF_DICE

    counts = [dice_results.count(value) for value in range(1, MAX_DICE_RESULT + 1)]

    assert sum(counts) == NUMBER_OF_DICE
    assert len(counts) == MAX_DICE_RESULT
    return counts


def calculate_score(counts: List[int]) -> int:
    """Calculate the simplified yatzy score for a given roll of 5 dice.

    The roll is given as a list of counts
    of how often each value appears in the roll.

    If all 5 dice show the same value,
    that's a yatzy, worth 50 points.

    Otherwise 3 of a kind is worth
    3 times the value that appears 3 or more times.

    Barring that, a pair is worth
    2 times the highest value that appears on 2 dice.

    If none of the above applies, the roll is worth 0 points.
    """

    highest_count = max(counts)
    if highest_count == NUMBER_OF_DICE:
        return YATZY

    highest_count = min(highest_count, 3)
    if 2 <= highest_count:
        return highest_count * find_most_frequent(counts)

    return 0


def find_most_frequent(counts: List[int]) -> int:
    """Find the value that appears most frequently on a roll of 5 dice.

    The roll is given as a list of counts
    of how often each value appears in the roll.

    In case of ties, select the highest value.
    """

    # A little more efficient way,
    # requiring only one pass rather than two.
    most_frequent_value = 0
    highest_count = 0
    for index, count in enumerate(counts):
        if count >= highest_count:
            highest_count = count
            most_frequent_value = index + 1

    return most_frequent_value


if __name__ == "__main__":
    main()
