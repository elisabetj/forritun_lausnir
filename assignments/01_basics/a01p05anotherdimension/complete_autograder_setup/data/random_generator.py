#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_x = float(sys.argv[1])
max_x = float(sys.argv[2])

d = random.uniform(min_x, max_x)

print("{:.2f}".format(d))
