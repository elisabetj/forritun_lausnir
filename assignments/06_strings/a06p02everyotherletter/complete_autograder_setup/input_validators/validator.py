#!/usr/bin/python3
from string import ascii_letters as letters, digits
import random
import sys

printable = letters + digits + " "
# because string.printable isn't actually printable and it also has LF and CR

s = sys.stdin.readline().strip()
assert 1 <= len(s) <= 10**6

assert not sys.stdin.read()

for char in s:
    assert char in printable

sys.exit(42)
