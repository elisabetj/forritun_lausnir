#!/usr/bin/python3
import random
import sys

from string import ascii_letters


def main():
    random.seed(sys.argv[-1])

    test_type = sys.argv[1]
    assert test_type in ["almostequal", "equal", "greater", "less"]
    min_n = int(sys.argv[2])
    max_n = int(sys.argv[3])

    first = random_string(min_n, max_n)
    second = random_string(min_n, max_n)

    if (first.lower() > second.lower() and test_type == "less") or (
        first.lower() < second.lower() and test_type == "greater"
    ):
        first, second = second, first
    elif test_type == "equal":
        second = first
    elif test_type == "almostequal":
        temp = list(first)
        temp[-1] = random.choice(list(set(ascii_letters) - {first[-1]}))
        second = "".join(temp)

    print(first)
    print(second)


def random_string(min_n, max_n):
    n = random.randint(min_n, max_n)
    return "".join(random.choices(ascii_letters, k=n))


if __name__ == "__main__":
    main()
