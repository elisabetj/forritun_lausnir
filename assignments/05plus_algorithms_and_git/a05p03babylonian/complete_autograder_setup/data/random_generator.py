#!/usr/bin/python3
import sys
import random 

random.seed(sys.argv[-1])

min_n = int(sys.argv[1])
max_n = int(sys.argv[2])
min_y = int(sys.argv[3])
max_y = int(sys.argv[4])

n = random.randint(min_n, max_n)
print(n)

g = random.randint(min_n, max_n)
print(g)

y = random.randint(min_y, max_y)
f = 10**(-y)
print(f"{f:f}".rstrip("0"))
