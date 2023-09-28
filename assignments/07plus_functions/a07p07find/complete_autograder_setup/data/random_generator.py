#!/usr/bin/python3
import sys
import random

from string import ascii_letters, digits, punctuation

printable = ascii_letters + digits + punctuation

random.seed(int(sys.argv[-1]))

min_length = int(sys.argv[1])
max_length = int(sys.argv[2])
min_k = int(sys.argv[3])
max_k = int(sys.argv[4])


length = random.randint(min_length, max_length)
occurrences = 0 if random.randint(0, 1) == 0 else random.randint(1, length)
k = random.randint(min_k, max_k)

element = random.choice(printable)
sequence = [element for _ in range(occurrences)] + [random.choice(printable) for _ in range(length - occurrences)]
random.shuffle(sequence)
s = ''.join(sequence)

print(s)
print(element)
print(k)
