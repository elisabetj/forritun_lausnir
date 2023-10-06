import sys

lines = sys.stdin.readlines()

assert len(lines) > 0

last_line = lines[-1].strip("\n").split(",")

try:
    last_line = map(int,last_line)
except ValueError:
    exit(1)

assert all([isinstance(n,int) for n in last_line])

exit(42)
