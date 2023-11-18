#!/usr/bin/python3
import random
import sys

from string import ascii_letters

random.seed(sys.argv[-1])

min_char_amount = int(sys.argv[1])
max_char_amount = int(sys.argv[2])

char_amount = random.randint(min_char_amount, max_char_amount)

char_set = ascii_letters + " \n"
weights = [2 for _ in ascii_letters] + [20,1]

output_str = "".join(random.choices(char_set, weights=weights, k=char_amount))

print(output_str)
