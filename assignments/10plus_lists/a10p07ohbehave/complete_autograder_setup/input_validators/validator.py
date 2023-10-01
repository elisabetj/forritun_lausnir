import sys
import re

lines = sys.stdin.readlines()

for line in lines:
    assert(re.search("[a-zA-Z]*",line))
exit(42)
