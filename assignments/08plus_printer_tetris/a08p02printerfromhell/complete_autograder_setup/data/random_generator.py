#!/usr/bin/python3
import random
import sys
import re

from string import ascii_letters

random.seed(sys.argv[-1])

valid_letters = ascii_letters + ",'?!"

min_n = int(sys.argv[1])
max_n = int(sys.argv[2])
min_m = int(sys.argv[3])
max_m = int(sys.argv[4])
test_type = sys.argv[5]

if test_type == "fixed_width":
    min_m = random.randint(min_m, max_m)
    max_m = min_m
elif test_type == "no_leading_spaces":
    pass
elif test_type == "leading_spaces":
    valid_letters += " " * 20
else:
    assert False, "Invalid test type"


def random_string(min_n, max_n):
    n = random.randint(min_n, max_n)
    return "".join(random.choices(valid_letters, k=n)).rstrip(" ")


n = random.randint(min_n, max_n)

lines = [random_string(min_m, max_m) for _ in range(n)]

for line in lines:
    print(line)
