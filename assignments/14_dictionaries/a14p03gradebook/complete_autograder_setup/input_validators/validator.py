import sys

REQUIRED_NUMBER_OF_LINES = 3

YES = "y"
NO = "n"


def main():
    lines = sys.stdin.readlines()
    lines = [line.rstrip() for line in lines]
    assert len(lines) >= REQUIRED_NUMBER_OF_LINES
    assert len(lines) % 3 == 0

    number_of_grades = len(lines) // 3
    for i in range(number_of_grades):
        email = lines[3 * i]
        grade = lines[3 * i + 1]
        more = lines[3 * i + 2]

        assert email.endswith("@ru.is")
        assert 9 <= len(email) <= 18

        assert grade.isdigit()
        grade = int(grade)
        assert 0 <= grade <= 10

        assert more in (YES, NO)
        if i < number_of_grades - 1:
            assert more == YES
        else:
            assert i == number_of_grades - 1
            assert more == NO

    exit(42)


if __name__ == "__main__":
    main()
