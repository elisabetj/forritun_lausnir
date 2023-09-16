#!/usr/bin/python3
import sys
import random

from string import ascii_lowercase

VOWELS = 'aeiouy'

def random_string():
    length = random.randint(1,20)
    split_index = random.randint(0, length - 1)
    prefix = random.choices(ascii_lowercase, k=split_index)
    vowel = random.choice(VOWELS)
    suffix = random.choices(ascii_lowercase, k=length - split_index - 1)
    characters = prefix + [vowel] + suffix
    return ''.join(characters)

random.seed(sys.argv[-1])

min_n = int(sys.argv[1])
max_n = int(sys.argv[2])
sentence = []

n = random.randint(min_n,max_n)

for _ in range(n):
    s = random_string()
    sentence.append(s)

print(" ".join(sentence))
