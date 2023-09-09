#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

min_num = int(sys.argv[1])
max_num = int(sys.argv[2])

x = random.randint(min_num, max_num)
print(x)
