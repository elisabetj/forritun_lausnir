#!/usr/bin/python3
from re import match
import sys

kLim = 100
nLim = 100
xiLim = 2000

k = sys.stdin.readline()
assert match('^-?[1-9][0-9]*\n$', k)
n = sys.stdin.readline()
assert match('^-?[1-9][0-9]*\n$', n)

k = int(k)
n = int(n)

assert abs(k) <= kLim
assert 1 <= n <= nLim

for i in range(n):
	xi = sys.stdin.readline()
	assert match('^[0-9]+\n$', xi), xi
	xi = int(xi)
	assert 0 <= xi <= xiLim

assert not sys.stdin.read()
sys.exit(42)
