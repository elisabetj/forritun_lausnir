#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_n = int(sys.argv[1])
max_n = int(sys.argv[2])
min_m = int(sys.argv[3])
max_m = int(sys.argv[4])

n = random.randint(min_n, max_n)
m = random.randint(min_m, max_m)
print(n)
print(m)
