#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

lower = int(sys.argv[1])
upper = int(sys.argv[2])
zeroDisc = int(sys.argv[3])

if zeroDisc:
	aSqrt = int(abs(random.randint(lower, upper))**0.5)
	cSqrt = int(abs(random.randint(lower, upper))**0.5)
	b = 2*aSqrt*cSqrt
	a = aSqrt**2
	c = cSqrt**2
else:
	a = random.randint(lower, upper)
	b = random.randint(lower, upper)
	c = random.randint(lower, upper)

print(a)
print(b)
print(c)
