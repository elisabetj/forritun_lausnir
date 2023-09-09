#!/usr/bin/python3
"""A program that calculates the distance between two points.

Prompts for four integers,
denoting the coordinates of two points in the plane,
calculates the distance, and prints the result.
"""

import math

x1: int = int(input())
y1: int = int(input())
x2: int = int(input())
y2: int = int(input())

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(d)
