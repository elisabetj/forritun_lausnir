#!/usr/bin/env python2
# coding: utf-8

import string
import random
import math
import sys

random.seed(int(sys.argv[-1]))

RANDOM = "rand"
AT_MOST = "atmost"
EVENLY_DISTRIBUTED = "sqrt"

CLOSE_TO_SQRT = "Sqrt."
ANYWHERE = "Any."


def main():
    method = sys.argv[1]
    if method == RANDOM:
        rand(
            number_of_entries=int(sys.argv[2]),
            length=int(sys.argv[3]),
            probability=float(sys.argv[4]),
        )
    elif method == AT_MOST:
        atmost(max_number_of_symbols=int(sys.argv[2]), strategy=ANYWHERE)
    elif method == EVENLY_DISTRIBUTED:
        atmost(max_number_of_symbols=int(sys.argv[2]), strategy=CLOSE_TO_SQRT)
    else:
        assert False, f"Unexpected method {method} requested."


def rand(number_of_entries, length, probability):
    entries = []
    print(number_of_entries)
    for iteration in range(number_of_entries):
        poll = random.uniform(0, 1)
        size = random.randint(1, length)
        if poll <= probability or iteration == 0:
            task = random_entry(size)
        else:
            task = random.choice(entries)
        entries.append(task)
        print(task)


def atmost(max_number_of_symbols: int, strategy: str) -> None:
    entry_length = fix_length(max_number_of_symbols, strategy)
    number_of_entries = max_number_of_symbols // entry_length
    print(number_of_entries)
    for _ in range(number_of_entries):
        print(random_entry(entry_length))


def fix_length(number_of_symbols: int, strategy: str) -> int:
    if strategy == CLOSE_TO_SQRT:
        return int(math.sqrt(number_of_symbols)) + random.randint(-10, 10)
    elif strategy == ANYWHERE:
        return random.randint(1, number_of_symbols)
    else:
        assert False, f"Unexpected strategy {strategy} encountered."


def random_entry(length: int) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


if __name__ == "__main__":
    main()
