#!/usr/bin/python3
import random
import sys
from math import sqrt


random.seed(sys.argv[-1])

def is_prime(n: int) -> bool:
    """Returns True if the number n is prime, False otherwise."""
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def random_numbers(amount, condition, min_n, max_n):
    ret_list = []
    for _ in range(amount):
        n = random.randint(min_n, max_n)
        while is_prime(n) == condition:
            n = random.randint(min_n, max_n)
        ret_list.append(n)
    return ret_list

min_length = int(sys.argv[1])
max_length = int(sys.argv[2])

min_digits = int(sys.argv[3])
max_digits = int(sys.argv[4])

test_type = sys.argv[5]

digits = []
digits_length = random.randint(min_length, max_length)

if test_type == "prime":
    digits = random_numbers(digits_length, False, min_digits, max_digits)

elif test_type == "noprime":
    digits = random_numbers(digits_length, True, min_digits, max_digits)

elif test_type == "mixed":
    digits = random_numbers(digits_length // 2, True, min_digits, max_digits)
    digits += random_numbers(digits_length // 2, False, min_digits, max_digits)
    random.shuffle(digits)

else:
    assert False, "Invalid test type"
    
print(",".join(map(str,digits)))

