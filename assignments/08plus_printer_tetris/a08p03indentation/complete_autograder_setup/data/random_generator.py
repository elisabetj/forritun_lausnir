#!/usr/bin/python3
import random
import sys
import re

from string import ascii_letters

valid = ascii_letters + ",'?!"

random.seed(sys.argv[-1])


def random_string(min_n, max_n):
    n = random.randint(min_n, max_n)
    return "".join(random.choices(valid, k=n))


min_lines = int(sys.argv[1])
max_lines = int(sys.argv[2])

new_line_amount = random.randint(min_lines, max_lines)

min_line_len = int(sys.argv[3])
max_line_len = int(sys.argv[4])

min_indent = int(sys.argv[5])
max_indent = int(sys.argv[6])
random_indent = random.randint(min_indent, max_indent)

string = ""
lines = []
for _ in range(new_line_amount):
    new_string = random_string(min_line_len, max_line_len)
    prefix_spaces = random.randint(0, 10) + abs(random_indent)
    if prefix_spaces > 70 - len(new_string):
        prefix_spaces = 70 - len(new_string)
    prefix = prefix_spaces * " "
    lines.append((prefix + new_string).rstrip())

print(random_indent)
for line in lines:
    print(line)
