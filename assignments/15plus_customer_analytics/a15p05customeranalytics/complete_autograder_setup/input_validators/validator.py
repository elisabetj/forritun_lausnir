import sys

lines = sys.stdin.readlines()
assert len(lines) == 1
filename = lines[0].rstrip()

assert (filename.endswith('.csv'))

exit(42)

