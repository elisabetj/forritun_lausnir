#!/usr/bin/python3
import random

length = int(input())

the_sum = 0
for i in range(1, length + 1):
    the_sum += 1 / 2**i
    print(the_sum + random.uniform(-2e-11, 2e-11))
