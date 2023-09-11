#!/usr/bin/python3

import random
import sys

random.seed(sys.argv[-1])
min_stop_range = int(sys.argv[1])
max_stop_range = int(sys.argv[2])
min_num_divisors = int(sys.argv[3])
max_num_divisors = int(sys.argv[4])

stop_range = random.randint(min_stop_range, max_stop_range)
num_divisors = random.randint(min_num_divisors, max_num_divisors)
print(stop_range)
print(num_divisors)
