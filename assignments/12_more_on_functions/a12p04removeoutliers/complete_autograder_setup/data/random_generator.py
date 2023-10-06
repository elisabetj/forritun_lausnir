#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

MIN_LENGTH = int(sys.argv[1])
MAX_LENGTH = int(sys.argv[2])
assert 1 <= MIN_LENGTH <= MAX_LENGTH < 1000

MIN_NUMBER = int(sys.argv[1])
MAX_NUMBER = int(sys.argv[2])
assert 0 <= MIN_NUMBER <= MAX_NUMBER <= 10000


def main():
    number_list = [
        str(random.randrange(MIN_NUMBER, MAX_NUMBER))
        for _ in range(random.randint(MIN_LENGTH, MAX_LENGTH))
    ]
    print(" ".join(number_list))


if __name__ == "__main__":
    main()
