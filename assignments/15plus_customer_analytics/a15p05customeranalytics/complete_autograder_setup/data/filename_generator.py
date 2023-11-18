#!/usr/bin/python3
import random
import sys
import string

random.seed(sys.argv[-1])  # Using the first argument for seeding.

filename_suffix = int(sys.argv[1]) # Using the second argument to determine the data type.
test_type = sys.argv[2]

filename = f"{test_type}-{filename_suffix:02d}.csv"

print(filename)
