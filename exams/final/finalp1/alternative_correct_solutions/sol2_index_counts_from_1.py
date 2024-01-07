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
    return [int(value) for value in line.split()]


def get_counts(dice: List[int]) -> List[int]:
    """Count how often each value appears.

    Return a list of counts
    for each possible outcome on a die roll,
    where the second count in the list
    (at position 1 in the output list)
    indicates how many 1's appear
    in the given list of dice results,
    the third count (at position 2)
    indicates how many 2's appear, and so on.
    The count list is as long as there are sides on the dice.

    For example, if the dice list is [3, 3, 4, 4, 1],
    then the count list is [0, 1, 0, 2, 2, 0, 0],
    indicating that the number 1 appears once,
    the numbers 3 and 4 appear twice each,
    but the numbers 2, 5 and 6 never appear.

    An extra, unused, zero is kept at the start of the resulting count list,
    for the porpose of making the indexes coincide with the die values.
    """
    assert len(dice) == NUMBER_OF_DICE
    assert 0 not in dice
    assert 1 <= min(dice) <= max(dice) <= MAX_DICE_RESULT

    counts = [dice.count(value) for value in range(MAX_DICE_RESULT + 1)]

    assert len(counts) == MAX_DICE_RESULT + 1
    assert counts[0] == 0
    assert sum(counts) == sum(counts[1:]) == NUMBER_OF_DICE
    return counts


def calculate_score(counts: List[int]) -> int:
    """Calculate the simplified yatzy score for a given roll of 5 dice."""
    if 5 in counts:
        return YATZY

    if max(counts) >= 3:
        for value, count in enumerate(counts):
            if count >= 3:
                assert value > 0
                return 3 * value

    if 2 in counts:
        for value in range(6, 0, -1):
            count = counts[value]
            if count == 2:
                return 2 * value

    return 0


if __name__ == "__main__":
    main()
