#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_i = int(sys.argv[1])
max_i = int(sys.argv[2])
min_n = int(sys.argv[3])
max_n = int(sys.argv[4])

n = random.randint(min_n, max_n)
for line in range(n-1):
    i = random.randint(min_i, max_i)
    if (i != 10):
        print(i)
print(10)
