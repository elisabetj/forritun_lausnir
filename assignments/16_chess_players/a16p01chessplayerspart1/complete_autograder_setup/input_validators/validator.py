import sys
from os import path

from typing import Tuple, List

REQUIRED_NUMBER_OF_LINES = 1
REQUIRED_NUMBER_OF_ITEMS_PER_LINE = 5
MAX_LENGTH_OF_NAME = 40

CURRENT_ASSIGNMENT = "16_chess_players"
CURRENT_PROBLEM = "a16p01chessplayerspart1"


def main() -> None:
    lines = sys.stdin.readlines()
    lines = [line.rstrip() for line in lines]
    assert len(lines) == REQUIRED_NUMBER_OF_LINES
    file_name = lines[0]
    assert file_name.endswith(".csv")
    validate_file(file_name=file_name)

    exit(42)


def validate_file(file_name: str) -> None:
    lines = read_file(file_name)

    previous_rating = float("inf")
    for index, line in enumerate(lines):
        full_name, rank, country, rating, birth_year = parse_line(line)

        assert len(full_name) <= MAX_LENGTH_OF_NAME

        assert rank == index + 1

        assert country.isupper()
        assert len(country) == 3

        assert rating <= previous_rating
        previous_rating = rating

        assert 1900 <= birth_year <= 2023


def read_file(file_name: str) -> List[str]:
    path_to_file = path.join(
        "Assignments",
        CURRENT_ASSIGNMENT,
        CURRENT_PROBLEM,
        "data",
        file_name,
    )
    with open(path_to_file) as file:
        return [line.strip() for line in file]


def parse_line(line: str) -> Tuple[str, int, str, int, int]:
    """Interprets a single line from the file."""

    items = [item.strip() for item in line.split(";")]
    assert len(items) == REQUIRED_NUMBER_OF_ITEMS_PER_LINE
    rank, name, country, rating, birth_year = items

    names = name.split(",")
    assert len(names) == 2
    last_name, first_name = [name.strip() for name in names]
    full_name = f"{first_name} {last_name}"

    assert rank.isnumeric()
    assert country.isalpha()
    assert rating.isnumeric()
    assert birth_year.isnumeric()

    return full_name, int(rank), country, int(rating), int(birth_year)


if __name__ == "__main__":
    main()
