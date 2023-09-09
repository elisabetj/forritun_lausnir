#!/usr/bin/python3
"""A program that calculates the volume of a hemisphere.

Prompts for a diameter, d (a float),
calculates the volume of half a sphere with diameter d,
and prints the result.
"""

pi = 3.1415926536

diameter = float(input())
radius = diameter / 2

volume_of_sphere = (4 / 3) * pi * (radius**3)
volume_of_hemisphere = volume_of_sphere / 2

print(f"{volume_of_hemisphere:.15f}")
