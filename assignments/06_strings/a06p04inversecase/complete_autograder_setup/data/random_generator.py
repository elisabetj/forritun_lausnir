#!/usr/bin/python3
from string import ascii_letters as letters, digits, punctuation
import random
import sys

printable = letters + digits + punctuation + " "
# because string.printable isn't actually printable and it also has LF and CR

random.seed(sys.argv[-1])

min_bound = int(sys.argv[1])
max_bound = int(sys.argv[2])

length = random.randrange(min_bound, max_bound)
s = random.choices(printable, k=length)

print("".join(s))
