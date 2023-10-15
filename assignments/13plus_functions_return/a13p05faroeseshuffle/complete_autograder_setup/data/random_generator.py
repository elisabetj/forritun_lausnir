#!/usr/bin/python3
from random import randint, randrange, seed, shuffle
import sys

seed(sys.argv[-1])

min_length = int(sys.argv[1])
max_length = int(sys.argv[2])
starting_half = sys.argv[3]
assert starting_half in ["top", "bottom"]
parity = int(sys.argv[4])
assert parity in [0, 1]

def main():
    length = randrange(min_length + min_length % 2 - parity, max_length+1, 2)
    number_list = list(range(1, length+1))
    shuffle(number_list)
    print(starting_half)
    print(length)
    print(' '.join(map(str, number_list)))


if __name__ == "__main__":
    main()
