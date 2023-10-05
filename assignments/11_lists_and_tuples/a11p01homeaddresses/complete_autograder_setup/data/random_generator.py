#!/usr/bin/python3
import random
import sys

from string import ascii_letters

random.seed(sys.argv[-1])


def random_string(min_n, max_n):
    n = random.randint(min_n, max_n)
    return "".join(random.choices(ascii_letters, k=n))


min_n = int(sys.argv[1])
max_n = int(sys.argv[2])


address_amount = random.randint(min_n, max_n)
for _ in range(address_amount):
    address_name = random_string(10, 12)
    address_nr = random.randint(1, 100)

    print(f"{address_name} {address_nr}")

print("q")
