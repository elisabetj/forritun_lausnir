import sys
import re

line = sys.stdin.readline().rstrip("\n")
indent_change = int(line)
assert str(indent_change) == line
assert -100 <= indent_change <= 100

line_count = 0
for line in sys.stdin:
    assert re.match("^([a-zA-Z,'?!()= ]{0,69}[a-zA-Z,'?!()=])?\n$", line), repr(line)
    line_count += 1

assert 1 <= line_count <= 70

assert not sys.stdin.read()

sys.exit(42)
