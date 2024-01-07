#!/usr/bin/python3

from typing import List

MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.
NUMBER_OF_DICE = 5
YATZY = 50


def main():
    while dice_values := input():
        print(calculate_score(dice_values))


def calculate_score(line: str) -> int:
    dice_values = [int(value) for value in line.split()]
    assert len(dice_values) == NUMBER_OF_DICE

    counts = get_counts(dice_results=dice_values)
    highest_count = max(counts)

    if highest_count == NUMBER_OF_DICE:
        return YATZY

    most_frequent_value = find_most_frequent(counts)

    if 2 <= highest_count <= 3:  # Ignores 4 of a kind.
        return highest_count * most_frequent_value

    return 0


def find_most_frequent(counts: List[int]) -> int:
    highest_count = max(counts)
    most_frequent_value = 0
    for i in range(MAX_DICE_RESULT):
        if counts[i] == highest_count:
            most_frequent_value = i + 1

    return most_frequent_value


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
