#!/usr/bin/env python2
# coding: utf-8

import string
import random
import math
import sys

random.seed(int(sys.argv[-1]))


def main():
    method = sys.argv[1]
    if method == "rand":
        rand(int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]))
    elif method == "atmost":
        atmost(int(sys.argv[2]))
    elif method == "sqrt":
        srt(int(sys.argv[2]))
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


def atmost(max_number_of_symbols):
    entry_length = random.randint(1, max_number_of_symbols)
    number_of_entries = max_number_of_symbols // entry_length
    print(number_of_entries)
    for _ in range(number_of_entries):
        print(random_entry(entry_length))


def srt(max_number_of_symbols):
    entry_length = int(math.sqrt(max_number_of_symbols)) + random.randint(-10, 10)
    number_of_entries = max_number_of_symbols // entry_length
    print(number_of_entries)
    for _ in range(number_of_entries):
        print(random_entry(entry_length))


def random_entry(length: int) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


if __name__ == "__main__":
    main()
