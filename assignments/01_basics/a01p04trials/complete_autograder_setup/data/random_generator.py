#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_x = int(sys.argv[1])
max_x = int(sys.argv[2])

while True:
    a = random.randint(min_x, max_x)
    b = random.randint(min_x, max_x)
    c = random.randint(min_x, max_x)
    L = sorted([a,b,c])
    if L[2] <= L[1] + L[0]:
        break

print("{}".format(a))
print("{}".format(b))
print("{}".format(c))
