#!/usr/bin/python3
import random
import sys

printable = ''.join([chr(i) for i in range(32, 127)])

random.seed(sys.argv[-1])

min_k = int(sys.argv[1])
max_k = int(sys.argv[2])
k = random.randint(min_k, max_k)

def random_string():
    n = random.randint(1, 50)
    return ''.join(random.choice(printable) for _ in range(n))

def shift(s, k):
    lo = ord(' ')
    hi = ord('~')
    m = hi-lo+1
    return ''.join(chr((ord(c) + k - lo) % m + lo) for c in s)

lines = ["Hail, Caesar!", random_string(), random_string(), random_string()]

for line in lines:
    print(shift(line, k))
