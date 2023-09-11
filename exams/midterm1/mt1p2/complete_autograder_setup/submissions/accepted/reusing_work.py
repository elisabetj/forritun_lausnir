#!/usr/bin/python3

RATIO = 1 / 2

number_of_lines = int(input())

total_sum = 0
new_term = 1
for line in range(number_of_lines):
    new_term *= RATIO
    total_sum += new_term
    print(total_sum)
