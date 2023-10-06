#!/usr/bin/python3
from typing import List


DIGITS = 4


def main():
    filename = input()
    file_object = open_file(filename)
    if file_object is not None:
        process_file(file_object)
        file_object.close()


def open_file(filename: str):
    """Opens the given file, returning its file object if found, otherwise None."""

    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return None


def process_file(file_object) -> None:
    """Processes the data given the file object and output analytics."""

    strings = get_data(file_object)
    numbers = get_floats(strings)
    cumulative_sums = get_cumulative_sums(numbers)
    median = get_median(numbers)

    print_numbers_rounded(numbers)
    print_numbers_rounded(cumulative_sums)
    print_numbers_rounded(sorted(numbers))
    if median != None:
        print(round(median, DIGITS))


def get_data(file_object) -> List[str]:
    """Returns a list of strings found in each line in the given file_oject."""

    lines = []
    for line in file_object:
        lines.append(line)

    return lines


def get_floats(strings: List[str]) -> List[float]:
    """Returns a new list which contains only the float numbers from str_list."""

    numbers = []
    for string in strings:
        try:
            float_num = float(string)
            numbers.append(float_num)
        except ValueError:
            continue

    return numbers


def get_cumulative_sums(numbers: List[float]) -> List[float]:
    """Returns the cumulative sum in num_list, i.e. a sequence of partial sums."""

    cumulative_sums = []
    cumulative_sum = 0

    for number in numbers:
        cumulative_sum += number
        cumulative_sums.append(cumulative_sum)

    return cumulative_sums


def get_median(numbers: List[float]) -> float | None:
    """Returns the median of num_list."""

    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    middle_index = length // 2
    return sorted_numbers[middle_index]


def print_numbers_rounded(numbers: List[float]) -> None:
    """Prints the contents of num_list, in a single line with one space between the elements."""

    if numbers == []:
        return

    for numbers in numbers:
        print(round(numbers, DIGITS), end=" ")
    print()


if __name__ == "__main__":
    main()
