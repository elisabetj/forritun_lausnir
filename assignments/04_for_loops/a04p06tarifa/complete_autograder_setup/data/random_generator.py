#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_m = int(sys.argv[1])
max_m = int(sys.argv[2])
min_n = int(sys.argv[3])
max_n = int(sys.argv[4])

m = random.randint(min_m, max_m)
n = random.randint(min_n, max_n)

print(m)
print(n)
total = 0

for _ in range(n):
    total += m
    d = random.randint(0, total)
    total -= d
    print(d)
