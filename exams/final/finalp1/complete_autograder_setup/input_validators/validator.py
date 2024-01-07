#!/usr/bin/python3
import sys

REQUIRED_NUMBER_OF_ITEMS_PER_LINE = 5


def main():
    lines = sys.stdin.readlines()
    lines = [line.rstrip("\n") for line in lines]

    last_line = lines.pop()
    assert not last_line
    assert 0 <= len(lines) <= 20

    for line in lines:
        assert line == line.strip()
        assert line.split() == line.split(" ")

        dice_results = line.split()
        assert len(dice_results) == REQUIRED_NUMBER_OF_ITEMS_PER_LINE

        for result in dice_results:
            assert not result.startswith("0")

            assert result.isnumeric()
            value = int(result)

            assert 1 <= value <= 6

    sys.exit(42)


if __name__ == "__main__":
    main()
