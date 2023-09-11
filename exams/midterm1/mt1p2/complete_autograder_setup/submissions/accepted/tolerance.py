#!/usr/bin/python3
import random

length = int(input())

the_sum = 0
for i in range(1, length + 1):
    the_sum += 1 / 2**i
    print(the_sum + random.uniform(-5e-12, 5e-12))
