#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

squarecnt = int(sys.argv[1])
print(random.randrange(squarecnt))
