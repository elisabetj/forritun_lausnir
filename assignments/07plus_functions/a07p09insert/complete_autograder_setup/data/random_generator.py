#!/usr/bin/python3
import sys
import random

from string import ascii_letters, digits, punctuation

printable = ascii_letters + digits + punctuation

random.seed(int(sys.argv[-1]))

min_length = int(sys.argv[1])
max_length = int(sys.argv[2])
test_type = sys.argv[3]

length = random.randint(min_length, max_length)

s = ''.join(random.choices(printable, k=length))
element = random.choice(printable)

if test_type == "first":
    i = 0
elif test_type == "last":
    i = len(s)
elif test_type == "random":
    i = random.randint(0, len(s))
else:
    assert False, "Invalid test type"

print(s)
print(i)
print(element)
