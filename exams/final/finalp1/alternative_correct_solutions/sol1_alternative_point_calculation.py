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
    if 5 in counts:
        return YATZY

    if max(counts) >= 3:
        for value, count in enumerate(counts, start=1):
            if count >= 3:
                return 3 * value

    if 2 in counts:
        for value in range(6, 0, -1):
            index = value - 1
            count = counts[index]
            if count == 2:
                # We're counting backwards, so we can return immediately,
                # as the first pair we see is also the highest pair.
                # And we've already checked for any 3-of-a-kind.
                return 2 * value

    return 0


if __name__ == "__main__":
    main()
