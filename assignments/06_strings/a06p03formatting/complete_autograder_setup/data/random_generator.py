#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_bound = int(sys.argv[1])
max_bound = int(sys.argv[2])
is_integer = int(sys.argv[3])


if is_integer:
    rand = random.randrange(min_bound, max_bound)
else:
    rand = random.random() * (max_bound - min_bound) + min_bound

print(rand)
