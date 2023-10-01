#!/usr/bin/python3
from re import match
import sys

while True:
	s = sys.stdin.readline().strip()
	if s == 'x':
		break
	assert 1 <= len(s) <= 100

assert not sys.stdin.read()
sys.exit(42)
