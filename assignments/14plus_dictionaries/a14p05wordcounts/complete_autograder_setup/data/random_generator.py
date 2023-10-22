#!/usr/bin/python3
import random
import sys
from string import ascii_letters

random.seed(sys.argv[-1])


def main():
    pass


def random_word():
    length = random.randrange(1, 10)
    return "".join(random.choices(ascii_letters, k=length))


if __name__ == "__main__":
    main()
