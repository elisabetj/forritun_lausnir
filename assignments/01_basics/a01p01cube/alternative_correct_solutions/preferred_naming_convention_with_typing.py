#!/usr/bin/python3
"""A program that takes an integer n as input and prints out its cube."""

# Python is not a typed language,
# and as such it is not strictly necessary to specify of which type each variable is,
# but it has these so-called type hints, or annotations,
# which can improve readability, giving the reader more clue about what's going on.
# But they do more than that, because they also inform automatic tools,
# which can verify the consistency of type specifications to a certain extent,
# as well as providing the programmer with more context-aware information.
# And with these, there's no need to append the type of the variable to the variable name.
number: int = int(input())

cube: int = number**3

print(cube)
