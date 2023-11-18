import sys
from os import path

from typing import List

REQUIRED_NUMBER_OF_LINES = 2
REQUIRED_NUMBER_OF_ITEMS_PER_LINE = 2


def main():
    lines = sys.stdin.readlines()
    lines = [line.rstrip() for line in lines]
    assert len(lines) == REQUIRED_NUMBER_OF_LINES

    line = lines[1]
    items = line.split(",")
    assert 1 <= len(items) <= REQUIRED_NUMBER_OF_ITEMS_PER_LINE

    exit(42)


if __name__ == "__main__":
    main()
