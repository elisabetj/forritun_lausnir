#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_d = int(sys.argv[1])
max_d = int(sys.argv[2])

d = random.randint(min_d, max_d)
print(d)
