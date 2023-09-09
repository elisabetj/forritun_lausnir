#!/usr/bin/python3
"""A program that takes an integer n as input and prints out its cube."""

# Including the type in the variable name can help beginners to keep track of what's what,
# but in practice, this is not recommended.
# Take a look at the alternative solution for a preferred naming convention.
number_str = input()
number_int = int(number_str)

cube_int = number_int**3

print(cube_int)
