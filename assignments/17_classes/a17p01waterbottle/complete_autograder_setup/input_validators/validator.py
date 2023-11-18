import sys
import re

lines = sys.stdin.readlines()
clean_lines = [line.strip() for line in lines]

assert 2 <= len(clean_lines) <= 4

assert clean_lines[0] in ["__init__", "__str__","fill","drink"]

assert clean_lines[1] in ["True","False"]

for line in clean_lines[2:] :
    assert re.search("[0-9]+(.[0-9]+)?", line)

exit(42)
