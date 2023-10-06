import sys

lines = sys.stdin.readlines()
lines = [line.rstrip() for line in lines]
assert len(lines) == 1

line = lines[0]
preferences = line.split(",")
assert len(preferences) == 3

for choice in preferences:
    assert len(choice) <= 30

exit(42)
