#!/usr/bin/python3
import random
import sys

from string import ascii_letters

random.seed(sys.argv[-1])

method_name = sys.argv[1]
test_type = int(sys.argv[2])

MIN_STR_LENGTH = 5
MAX_STR_LENGTH = 12


def main():
    if method_name in ["__init__", "__str__"]:
        print(method_name)
        print(band := random_str())
        print(title := random_str())
        print(random_year())
        print(test_type)
    else:
        assert False, f"Invalid method name {method_name}."


def random_str(min_len=MIN_STR_LENGTH, max_len=MAX_STR_LENGTH):
    str_len = random.randint(min_len, max_len)
    return "".join(random.choices(ascii_letters, k=str_len))


def random_year():
    return random.randint(1930, 2023)


if __name__ == "__main__":
    main()
