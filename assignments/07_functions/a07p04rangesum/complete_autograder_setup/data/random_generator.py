#!/usr/bin/python3
import random
import sys


random.seed(sys.argv[-1])

min_n = int(sys.argv[1])
max_n = int(sys.argv[2])
step = int(sys.argv[3])

n_start = random.randint(min_n, max_n)
n_end = random.randint(n_start, max_n)

print(n_start)
print(n_end)
print(step)
