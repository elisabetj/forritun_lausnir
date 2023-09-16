#!/usr/bin/python3
from string import ascii_lowercase
import random
import sys

random.seed(sys.argv[-1])

min_bound = int(sys.argv[1])
max_bound = int(sys.argv[2])
is_palindrome = int(sys.argv[3])  # If odd, make palindrome.

length = random.randint(min_bound, max_bound)
if is_palindrome & 1:
    half_length = length // 2

    first_half = random.choices(ascii_lowercase, k=half_length)
    second_half = first_half[::-1]
    middle = random.choice(ascii_lowercase) if length % 2 else ""

    s = first_half + [middle] + second_half
else:
    s = random.choices(ascii_lowercase, k=length)

print("".join(s))
