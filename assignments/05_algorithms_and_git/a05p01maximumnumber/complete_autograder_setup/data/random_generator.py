#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_x = int(sys.argv[1])
max_x = int(sys.argv[2])

min_lines = int(sys.argv[3])
max_lines = int(sys.argv[4])

lines = random.randint(min_lines, max_lines)
for _ in range(lines):
    x = random.randint(min_x, max_x)
    print(x)
negative = random.randint(1, 1000) * -1
print(negative)
