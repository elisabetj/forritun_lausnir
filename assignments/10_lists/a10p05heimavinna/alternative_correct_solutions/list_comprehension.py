#!/usr/bin/env python3


def main():
    problems_specification = input()

    number_of_problems = 0
    for subspecification in problems_specification.split(";"):
        if "-" in subspecification:
            start, end = [int(problem) for problem in subspecification.split("-")]
            number_of_problems += end - (start - 1)
        else:
            number_of_problems += 1

    print(number_of_problems)


if __name__ == "__main__":
    main()
