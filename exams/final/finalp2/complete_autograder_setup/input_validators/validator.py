import sys
from os import path

from typing import List, Tuple

REQUIRED_NUMBER_OF_LINES = 1
REQUIRED_NUMBER_OF_ITEMS_PER_LINE = 3
MAX_LENGTH_OF_NAME = 20

CURRENT_ASSIGNMENT = "final"
CURRENT_PROBLEM = "finalp2"


def main():
    lines = sys.stdin.readlines()
    assert len(lines) == REQUIRED_NUMBER_OF_LINES
    (file_name,) = lines

    assert file_name.endswith("\n") and not file_name.endswith("\n\n")
    file_name = file_name.rstrip("\n")
    assert file_name == file_name.strip()
    assert file_name.endswith(".txt")
    validate_file(file_name=file_name)

    exit(42)


def validate_file(file_name: str) -> None:
    if file_name == "test17.txt":
        # This file intentionally does not exist.
        return

    lines = read_file(file_name)
    assert len(lines) >= 1

    counts = {}

    for line in lines:
        name, throw = parse_line(line)
        assert len(name) <= MAX_LENGTH_OF_NAME
        assert 50 <= throw <= 75

        if name not in counts:
            counts[name] = 0

        counts[name] += 1

    for count in counts.values():
        assert 1 <= count <= 4


def read_file(file_name: str) -> List[str]:
    path_to_file = path.join(
        "Exams",
        CURRENT_ASSIGNMENT,
        CURRENT_PROBLEM,
        "data",
        file_name,
    )
    with open(path_to_file) as file:
        return [line for line in file]


def parse_line(line: str) -> Tuple[str, float]:
    """Interprets a single line from the file."""

    assert line.endswith("\n") and not line.endswith("\n\n")
    line = line.rstrip("\n")
    assert line == line.strip()
    assert line.split() == line.split(" ")
    items = line.split()
    assert len(items) == REQUIRED_NUMBER_OF_ITEMS_PER_LINE
    first_name, last_name, throw = items
    full_name = f"{first_name} {last_name}"

    parts = throw.split(".")
    assert len(parts) <= 2
    for part in parts:
        assert part.isnumeric()

    if len(parts) == 2:
        _, decimals = parts
        assert len(decimals) <= 2

    return full_name, float(throw)


if __name__ == "__main__":
    main()
