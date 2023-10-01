#!/usr/bin/python3
import random
import sys


random.seed(sys.argv[-1])


min_n = int(sys.argv[1])
max_n = int(sys.argv[2])

a = random.randint(min_n, max_n)

print(a)
