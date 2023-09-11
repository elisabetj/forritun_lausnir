#!/usr/bin/python3

import random
import sys

random.seed(sys.argv[-1])

how_often = random.randint(1, 20)
for _ in range(how_often):
    price = round(random.uniform(1, 1000), 1)
    print(price)

print(0)
