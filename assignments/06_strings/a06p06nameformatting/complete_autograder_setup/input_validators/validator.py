#!/usr/bin/python3
from string import digits
import random
import sys
import re

s = sys.stdin.readline().strip()
assert re.match(r"^[a-z]+, [a-z]+$", s)
assert 4 <= len(s) <= 10**6, len(s)

assert not sys.stdin.read()

sys.exit(42)
