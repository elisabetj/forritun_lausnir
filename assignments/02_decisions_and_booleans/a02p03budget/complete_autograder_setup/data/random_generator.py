#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

lower = int(sys.argv[1])
upper = int(sys.argv[2])

budget = random.randint(lower, upper)
p_1 = random.randint(lower, upper)
p_2 = random.randint(lower, upper)
p_3 = random.randint(lower, upper)

print(budget)
print(p_1)
print(p_2)
print(p_3)
