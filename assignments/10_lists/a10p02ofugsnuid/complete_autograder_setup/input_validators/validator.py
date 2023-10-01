#!/usr/bin/env python

import re
import sys

line = sys.stdin.readline()
assert re.match('^[1-9][0-9]*\n$', line)
n = int(line)
assert 1 <= n <= 2*10**5
for x in range(n):
    a = int(sys.stdin.readline())
    assert 0 <= a <= 10**9

assert sys.stdin.read() == ''
sys.exit(42)
