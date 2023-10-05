#!/usr/bin/python3
import random
import sys

from string import ascii_letters, digits, punctuation

letters = ascii_letters  + punctuation.replace(',','')

random.seed(sys.argv[-1])

min_length = int(sys.argv[1])
max_length = int(sys.argv[2])
test_type = sys.argv[3]

length = random.randint(min_length,max_length)

s = ""

if test_type == "numbers":
    for _ in range(length):
        elem_len = random.randint(1, 6)
        s += "".join(random.choices(digits ,k = elem_len)) + ","

elif test_type == "letters":
    for _ in range(length):
        elem_len = random.randint(1, 6)
        s += "".join(random.choices(letters ,k = elem_len)) + ","

elif test_type == "empty_mixed":
    for _ in range(length):
        elem_len = random.randint(1, 6)
        letters_or_digits = random.randint(0,2)
        if letters_or_digits == 0:
            s += "".join(random.choices(digits ,k = elem_len)) + ","
        elif letters_or_digits == 1:
            s += "".join(random.choices(letters ,k = elem_len)) + ","
        else:
            s += ","


elif test_type == "mixed":
    for _ in range(length):
        elem_len = random.randint(1, 6)
        letters_or_digits = random.randint(0,1)
        if letters_or_digits:
            s += "".join(random.choices(digits ,k = elem_len)) + ","
        else:
            s += "".join(random.choices(letters ,k = elem_len)) + ","

else:
    assert False, "Invalid test type"


s = s.rstrip(",")
print(s)
