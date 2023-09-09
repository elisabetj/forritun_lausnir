#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_k = int(sys.argv[1])
max_k = int(sys.argv[2])
min_n = int(sys.argv[3])
max_n = int(sys.argv[4])
min_x = int(sys.argv[5])
max_x = int(sys.argv[6])

k = random.randint(min_k, max_k)
n = random.randint(min_n, max_n)

print(k)
print(n)

for _ in range(n):
    x = random.randint(min_x, max_x)
    print(x)
