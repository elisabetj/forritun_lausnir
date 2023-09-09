#!/usr/bin/python3
import sys
import random 

random.seed(sys.argv[-1])

min_x = int(sys.argv[1])
max_x = int(sys.argv[2])

min_y = int(sys.argv[3])
max_y = int(sys.argv[4])


repeat = random.randint(min_y, max_y)
for _ in range(repeat):
    x = random.randint(min_x, max_x)
    print(x)

print("-1")
