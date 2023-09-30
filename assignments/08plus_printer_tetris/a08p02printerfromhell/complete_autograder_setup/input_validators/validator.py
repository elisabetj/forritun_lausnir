import sys
import re

line_count = 0
for line in sys.stdin:
    assert re.match("^([a-zA-Z,'?! ]{0,99}[a-zA-Z,'?!])?\n$", line)
    line_count += 1

assert 1 <= line_count <= 100

assert not sys.stdin.read()
sys.exit(42)
