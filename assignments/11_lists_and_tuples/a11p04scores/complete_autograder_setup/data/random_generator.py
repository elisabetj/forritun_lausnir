#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])


min_length = int(sys.argv[1])
max_length = int(sys.argv[2])

min_float = float(sys.argv[1])
max_float = float(sys.argv[2])

sequence_len = random.randint(min_length, max_length)

sequence = [str(round(random.uniform(max_float, min_float),1)) + " " for _ in range(sequence_len)]

print(''.join(sequence).rstrip())
