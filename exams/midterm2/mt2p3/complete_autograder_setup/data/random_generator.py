#!/usr/bin/python3

import random
import sys
import string

random.seed(sys.argv[-1])
num_integers = int(sys.argv[1])
max_int = int(sys.argv[2])

for _ in range(num_integers):
    num = random.randint(1, max_int)
    print(num)