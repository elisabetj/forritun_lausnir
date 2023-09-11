#!/usr/bin/python3

import random
import sys

random.seed(sys.argv[-1])

price_of_item = random.randint(1, 100)
amount_paid = random.randint(price_of_item, 100)

print(price_of_item)
print(amount_paid)
