#!/usr/bin/python3
import random
import sys
from itertools import combinations
from string import ascii_letters, digits

ALPHANUMERIC = ascii_letters + digits

random.seed(sys.argv[-1])

filename = sys.argv[1]
test_type = sys.argv[2]
min_ops = int(sys.argv[3])
max_ops = int(sys.argv[4])

SHOW = "show"
YEAR = "year"
CHANGE = "change"
SHOW_OP = "1"
YEAR_OP = "2"
CHANGE_OP = "3"

OTHER_OPS = [''.join(comb) for i in range(1, 4) for comb in combinations(ALPHANUMERIC, i)]
OTHER_OPS.remove(SHOW_OP)
OTHER_OPS.remove(YEAR_OP)
OTHER_OPS.remove(CHANGE_OP)

choices = test_type.split("_")
assert len(choices) == len(set(choices))
assert set(choices) <= set((SHOW, YEAR, CHANGE))

def main():
    print(filename)
    number_of_ops = random.randint(min_ops, max_ops)
    for _ in range(number_of_ops - 1):
        op = random.choice(choices)
        if op == SHOW:
            print(SHOW_OP)
        elif op == YEAR:
            print(YEAR_OP)
            print(random_year())
        elif op == CHANGE:
            print(CHANGE_OP)
            print(random_change())
    
    if number_of_ops > 0:
        print(random.choice(OTHER_OPS))


def random_year():
    MIN_YEAR = 1900
    MAX_YEAR = 2023
    return random.randint(MIN_YEAR, MAX_YEAR)


def random_change():
    MIN_VALUE = -10.0
    MAX_VALUE = 10.0
    MAX_DIGITS = 6
    return round(random.uniform(MIN_VALUE, MAX_VALUE), MAX_DIGITS)


if __name__ == "__main__":
    main()
