#!/usr/bin/python3

from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.
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
    """Count how often each value appears."""
    return [dice.count(value) for value in range(1, MAX_DICE_RESULT + 1)]


def calculate_score(counts: List[int]) -> int:
    """Calculate the simplified yatzy score for a given roll of 5 dice."""
    points = 0

    for die_value, count in enumerate(counts, start=1):
        if count == 5:
            # Jackpot. Return immediately.
            return YATZY

        if count >= 3:
            assert 3 <= count <= 4
            # We treat four of a kind as a three of a kind,
            # as per the instructions.

            # There is no room for anything better,
            # so we can return immediately.
            return 3 * die_value

        if count == 2:
            # We must not return immediately,
            # as there might be another higher pair coming,
            # or a three of a kind.
            points = 2 * die_value

    return points


if __name__ == "__main__":
    main()
