#!/usr/bin/python3

from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.
YATZY = 50


def main():
    """Print simplified yatzy score for a sequence of dice rolls."""
    dice = get_roll()
    while dice:
        assign_score(dice)

        dice = get_roll()


def get_roll() -> List[int]:
    """Parse a line containing dice results into a list of integers."""
    return [int(value) for value in input().split()]


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

        elif count >= 3:
            # If, elif, does not matter, becuase of the earlier return.
            return 3 * die_value

        elif count == 2:  # Ditto.
            points = 2 * die_value

    return points


def get_counts(dice: List[int]) -> List[int]:
    """Count how often each value appears."""
    return [dice.count(value) for value in range(MAX_DICE_RESULT + 1)]


if __name__ == "__main__":
    main()
