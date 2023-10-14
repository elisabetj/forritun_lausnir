from typing import List


def main() -> None:
    list_of_strings = get_input()
    list_of_numbers = extract_numbers(list_of_strings)
    missing_numbers = find_missing(list_of_numbers)
    display_output(list_of_strings, list_of_numbers, missing_numbers)


def get_input() -> List[str]:
    return input().split()


def extract_numbers(input_list: List[str]) -> List[int]:
    return [int(string) for string in input_list if is_number(string)]


def is_number(string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False


def find_missing(numbers: List[int]) -> List[int]:
    highest = max(numbers)
    return [number for number in range(highest) if number not in numbers]


def display_output(
    strings: List[str],
    numbers: List[int],
    missing: List[int],
) -> None:
    for output_list in strings, numbers, missing:
        print(output_list)


if __name__ == "__main__":
    main()
