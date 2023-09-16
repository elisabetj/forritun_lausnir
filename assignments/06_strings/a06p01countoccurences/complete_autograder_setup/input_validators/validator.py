#!/usr/bin/python3
import sys
from string import ascii_letters, digits, punctuation

valid_symbols = ascii_letters + digits + punctuation + " "

s = sys.stdin.readline().strip("\n")
assert len(s) <= 10**6
for symbol in s:
    assert symbol in valid_symbols, repr(symbol)
c = sys.stdin.readline().strip("\n")
assert len(c) == 1
assert c in valid_symbols, repr(c)

assert not sys.stdin.read()
sys.exit(42)
