#!/usr/bin/python3
"""A program that calculates the area of a triangle.

Prompts for three floats,
denoting the lengths of the sides of a triangle,
calculates the area, and prints the result.
"""

import math

a_str = input()
b_str = input()
c_str = input()

# Convert values to float.
a_float, b_float, c_float = float(a_str), float(b_str), float(c_str)

s = (a_float + b_float + c_float) / 2
area = math.sqrt(s * (s - a_float) * (s - b_float) * (s - c_float))

print(area)
