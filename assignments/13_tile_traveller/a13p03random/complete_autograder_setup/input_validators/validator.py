import sys

MAX_NUMBER_OF_GAMES = 10
YES = "y"
NO = "n"


def main():
    lines = sys.stdin.readlines()
    lines = [line.rstrip() for line in lines]
    number_of_lines = len(lines)
    assert 2 <= number_of_lines <= 1 + MAX_NUMBER_OF_GAMES

    number_of_yes = 0
    number_of_nos = 0
    for index, line in enumerate(lines):
        if index == 0:
            assert 0 <= int(line) <= 10000
        elif index < number_of_lines - 1:
            assert line.lower() == YES
        else:
            assert line.lower() == NO

        if line.lower() == YES:
            number_of_yes += 1
            assert index < number_of_lines - 1
        elif line.lower() == NO:
            number_of_nos += 1
            assert index == number_of_lines - 1

    assert number_of_nos == 1
    assert number_of_yes == number_of_lines - 2

    exit(42)


if __name__ == "__main__":
    main()
