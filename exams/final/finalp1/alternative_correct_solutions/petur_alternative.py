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
    """Count how often each value appears."""
    return [dice.count(value) for value in range(1, MAX_DICE_RESULT + 1)]


def calculate_score(counts: List[int]) -> int:
    """Calculate the simplified yatzy score for a given roll of 5 dice."""
    highest_count = max(counts)
    if highest_count == NUMBER_OF_DICE:
        return YATZY

    highest_count = min(highest_count, 3)
    if 2 <= highest_count:
        return highest_count * find_most_frequent(counts)

    return 0


def find_most_frequent(counts: List[int]) -> int:
    """Find the highest value that appears most frequently on a roll."""
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
