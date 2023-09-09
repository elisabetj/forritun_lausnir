#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

lower = int(sys.argv[1])
upper = int(sys.argv[2])

elo = random.randint(lower, upper)

print(elo)
