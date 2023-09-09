#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_x = int(sys.argv[1])
max_x = int(sys.argv[2])
min_y = int(sys.argv[3])
max_y = int(sys.argv[4])


x1 = random.randint(min_x, max_x)
y1 = random.randint(min_y, max_y)
x2 = random.randint(min_x, max_x)
y2 = random.randint(min_y, max_y)
print(x1)
print(y1)
print(x2)
print(y2)
