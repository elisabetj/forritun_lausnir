#!/usr/bin/python3
from re import match
import sys

mLim = 1000000
nLim = 100000

m = sys.stdin.readline()
assert match('^-?[1-9][0-9]*\n$', m)
n = sys.stdin.readline()
assert match('^-?[1-9][0-9]*\n$', n)

m = int(m)
n = int(n)

assert 1 <= m <= mLim
assert 1 <= n <= nLim
total = 0

for i in range(n):
	total += m
	d = sys.stdin.readline()
	assert match('^[0-9]+\n$', d), d
	d = int(d)
	total -= d
	assert total >= 0

assert not sys.stdin.read()
sys.exit(42)
