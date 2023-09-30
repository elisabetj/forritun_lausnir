#!/usr/bin/python3
import random
import sys
import string

random.seed(sys.argv[-1])  # Using the first argument for seeding.

filename_suffix = int(sys.argv[1]) # Using the second argument to determine the data type.

filename = f"test_file_{filename_suffix:02d}.txt"

print(filename)
