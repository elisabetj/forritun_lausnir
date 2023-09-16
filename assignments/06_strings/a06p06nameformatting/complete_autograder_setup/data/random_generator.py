#!/usr/bin/python3
from string import ascii_lowercase as letters
import random
import sys

random.seed(sys.argv[-1])

min_length_of_each_name = int(sys.argv[1])
max_length_of_each_name = int(sys.argv[2])

firstname_len = random.randint(min_length_of_each_name, max_length_of_each_name)
firstname = "".join(random.choices(letters, k=firstname_len))

lastname_len = random.randint(min_length_of_each_name, max_length_of_each_name)
lastname = "".join(random.choices(letters, k=lastname_len))

print(f"{lastname}, {firstname}")
