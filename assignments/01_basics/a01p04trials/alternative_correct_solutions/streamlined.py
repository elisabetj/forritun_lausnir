#!/usr/bin/python3
"""A program that calculates the area of a triangle.

Prompts for three floats,
denoting the lengths of the sides of a triangle,
calculates the area using Heron's formula, and prints the result.

Heron's formula gives the area, $A$, of a triangle with sides $a$, $b$, and $c$
as $A = \sqrt{s(s-a)(s-b)(s-c)}$
where $s = (a+b+c)/2$.
"""

import math

# Here, single-letter variables are acceptable,
# since these refer to a well established mathematical convention for this specific problem,
# and since the formula is explicitly given above.
# See also:
# https://google.github.io/styleguide/pyguide.html#3165-mathematical-notation
a: float = float(input())
b: float = float(input())
c: float = float(input())

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(area)
