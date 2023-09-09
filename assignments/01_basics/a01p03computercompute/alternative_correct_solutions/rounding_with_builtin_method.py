#!/usr/bin/python3
"""A program that calculates the distance between two points.

Prompts for four integers,
denoting the coordinates of two points in the plane,
calculates the distance, and prints the result.
"""

import math

x1_str = input()
y1_str = input()
x2_str = input()
y2_str = input()

x1_int = int(x1_str)
y1_int = int(y1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)

d = math.sqrt((x1_int - x2_int) ** 2 + (y1_int - y2_int) ** 2)
# Rounding to, say, 15 digits after the decimal point also works,
# since the autograder was set to judge these as numbers, not text,
# and is set to allow for a rounding error of 10**(-9),
# which can be expressed in Python using scientific notation, 1e-9.
print(round(d, 15))
