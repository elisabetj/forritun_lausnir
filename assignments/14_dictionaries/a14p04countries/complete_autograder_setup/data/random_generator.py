#!/usr/bin/python3
import random
import sys
from string import ascii_letters

random.seed(sys.argv[-1])

MIN_WRONG = int(sys.argv[1])
MAX_WRONG = int(sys.argv[2])
assert 0 <= MIN_WRONG <= MAX_WRONG
NUM_WRONG = random.randint(MIN_WRONG, MAX_WRONG)

MIN_QUERIES = int(sys.argv[3])
MAX_QUERIES = int(sys.argv[4])
assert 1 <= MIN_QUERIES <= MAX_QUERIES
NUM_QUERIES = random.randint(MIN_QUERIES, MAX_QUERIES)

CORRECT = "countries.txt"
CHAR_POOL = ascii_letters
YES = "y"
NO = "n"


def main():
    print_file_name()
    print_queries()


def print_file_name() -> None:
    for _ in range(NUM_WRONG):
        print(incorrect_file_name())

    print(CORRECT)


def incorrect_file_name() -> None:
    file_name = random_file_name()
    while file_name == CORRECT:
        file_name += random_file_name()

    return file_name


def random_file_name() -> str:
    return "".join(random.choices(CHAR_POOL, k=random_length()))


def print_queries() -> None:
    for _ in range(NUM_QUERIES - 1):
        print(random_length())
        print(YES)

    print(random_length())
    print(NO)


def random_length() -> int:
    return random.randint(1, 30)


if __name__ == "__main__":
    main()
