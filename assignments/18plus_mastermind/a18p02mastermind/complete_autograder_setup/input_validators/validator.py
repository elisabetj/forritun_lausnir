import sys
import re

lines = sys.stdin.readlines()
clean_lines =[line.strip() for line in lines]

seed = clean_lines[0]
rest = clean_lines[1:]

assert re.search("[0-9]{1,30}",seed)

for entry in rest:
    assert re.search("[a-zA-Z]{1,10}",entry)

exit(42)
