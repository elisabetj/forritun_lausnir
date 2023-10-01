#!/usr/bin/env python3


def main():
    problems_specification = input()

    number_of_problems = 0
    for subspecification in problems_specification.split(";"):
        if "-" in subspecification:
            left, right = subspecification.split("-")
            start, end = int(left), int(right)
            number_of_problems += end - (start - 1)
        else:
            number_of_problems += 1

    print(number_of_problems)


if __name__ == "__main__":
    main()
