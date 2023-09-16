#!/usr/bin/python3
import random
import sys
from string import ascii_letters as letters, digits

printable = letters + digits + " "
# because string.printable isn't actually printable and it also has LF and CR

random.seed(sys.argv[-1])

min_len = int(sys.argv[1])
max_len = int(sys.argv[2])

length = random.randrange(min_len, max_len)
print("".join(random.choices(printable, k=length)))
