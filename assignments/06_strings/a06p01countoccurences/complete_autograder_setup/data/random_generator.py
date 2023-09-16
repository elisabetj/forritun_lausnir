#!/usr/bin/python3
import random
import sys
from string import ascii_letters as letters, digits, punctuation

printable = letters + digits + punctuation + " "
# because string.printable isn't actually printable and it also has LF and CR

random.seed(sys.argv[-1])

min_len = int(sys.argv[1])
max_len = int(sys.argv[2])
test_type = sys.argv[3]

length = random.randint(min_len, max_len)
if test_type == "nomatch":
    c = random.choice(printable)
    distribution = printable.replace(c, "")
    s = "".join(random.choices(distribution, k=length))
    assert c not in s
elif test_type == "match":
    s = "".join(random.choices(printable, k=length))
    c = random.choice(s)
    assert c in s
elif test_type == "repeat":
    c = random.choice(printable)
    s = c * length
else:
    assert False

print(s)
print(c)
