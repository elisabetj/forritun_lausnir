#!/usr/bin/python3

RATIO = 1 / 2

length = int(input())

the_sum = 0
for i in range(1, length + 1):
    the_sum += RATIO**i
    print(the_sum)
