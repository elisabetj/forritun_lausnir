#!/usr/bin/python3
import random
import sys
import string

random.seed(sys.argv[-1])  # Using the first argument for seeding.

min_chars = 1
max_chars = 1000
char_count = random.randint(1, 1000)
printable = string.ascii_letters + " \n"
weights = [2 for _ in string.ascii_letters] + [10, 1]
print("".join(random.choices(printable, weights=weights, k=char_count)))
