#!/usr/bin/python3
from string import ascii_lowercase
import random
import sys
import re

s = sys.stdin.readline().strip()
assert 1 <= len(s) <= 10**5

for c in s:
    assert c in ascii_lowercase, repr(c)

assert not sys.stdin.read()

sys.exit(42)
