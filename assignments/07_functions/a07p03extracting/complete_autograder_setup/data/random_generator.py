#!/usr/bin/python3
import random
import sys

from string import ascii_letters, digits

mixed = ascii_letters + digits

random.seed(sys.argv[-1])
total_size = random.randint(1, 100)

desired_outcome = sys.argv[1]
assert desired_outcome in ("nonumberincluded", "numberincluded")

if desired_outcome == "numberincluded":
    length_of_first_number = random.randint(1, total_size)
    length_of_prefix = random.randint(0, total_size - length_of_first_number)
    length_of_suffix = total_size - length_of_first_number - length_of_prefix

    rand_prefix = "".join(random.choices(ascii_letters, k=length_of_prefix))
    rand_digits = "".join(random.choices(digits, k=length_of_first_number))
    rand_suffix = "".join(random.choices(mixed, k=length_of_suffix))
    while rand_suffix and rand_suffix[0].isnumeric():
        rand_suffix = "".join(random.choices(mixed, k=length_of_suffix))

    print(f"{rand_prefix}{rand_digits}{rand_suffix}")

else:
    assert desired_outcome == "nonumberincluded"

    random_letters = "".join(random.choices(ascii_letters, k=total_size))
    print(random_letters)
