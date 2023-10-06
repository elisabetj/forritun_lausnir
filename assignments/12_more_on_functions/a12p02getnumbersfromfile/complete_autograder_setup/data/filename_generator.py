#!/usr/bin/python3
import random
import sys
from string import ascii_letters


random.seed(sys.argv[-1])  # Using the first argument for seeding.

# Using the second argument to determine the data type.
filename_suffix = int(sys.argv[1])
filename = f"test_file_{filename_suffix:02d}.txt"


def main():
    for _ in range(random.randrange(20)):
        print(random_word())

    print(filename)

    for _ in range(random.randrange(5)):
        print(random_word())


def random_word():
    length = random.randrange(1, 10)
    return "".join(random.choices(ascii_letters, k=length))


if __name__ == "__main__":
    main()
