#!/usr/bin/python3
from string import ascii_letters, digits, punctuation
import random
import sys
import re

valid = ascii_letters + digits + punctuation + " "

s = sys.stdin.readline().strip("\n")
assert 1 <= len(s) <= 10**6

for c in s:
    assert c in valid, repr(c)

assert not sys.stdin.read()

sys.exit(42)
