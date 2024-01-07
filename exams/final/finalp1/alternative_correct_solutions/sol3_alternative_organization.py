#!/usr/bin/python3

from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.
NUMBER_OF_DICE = 5
YATZY = 50


def main():
    """Print simplified yatzy score for a sequence of dice rolls."""
    while dice := get_roll():
        assign_score(dice)


def get_roll() -> List[int]:
    """Parse a line containing dice results into a list of integers."""
    dice = [int(value) for value in input().split()]
    assert len(dice) == NUMBER_OF_DICE or not dice
    return dice


def assign_score(dice: List[int]) -> None:
    """Print the simplified yatzy score for a given roll of 5 dice."""
    score = calculate_score(dice)
    print(score)


def calculate_score(dice_values: List[int]) -> int:
    """Calculate the simplified yatzy score for a given roll of 5 dice."""
    counts = get_counts(dice_values)
    points = 0

    for die_value, count in enumerate(counts):
        if count == 5:
            return YATZY

        if count >= 3:
            return 3 * die_value

        if count == 2:
            points = 2 * die_value

    return points


def get_counts(dice: List[int]) -> List[int]:
    """Count how often each value appears."""
    return [dice.count(value) for value in range(MAX_DICE_RESULT + 1)]


if __name__ == "__main__":
    main()
