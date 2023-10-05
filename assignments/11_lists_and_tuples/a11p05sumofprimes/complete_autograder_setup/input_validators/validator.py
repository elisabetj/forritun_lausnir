import sys

lines = ','.join(sys.stdin.readlines()).rstrip("\n").split(",")

lines = [int(line) for line in lines]

assert 1 <= len(lines) <= 100

for line in lines:
    assert 1 <= line <= 100000


sys.exit(42)
