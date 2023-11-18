#!/usr/bin/env python

import re
import sys

line = sys.stdin.readline()
assert re.match("^[1-9][0-9]*\n$", line)
n = int(line)
tasks = [i for i in sys.stdin]
assert n == len(tasks)
for task in tasks:
    assert re.match("^[a-zA-Z0-9 ,.?]+\n$", task)
sys.exit(42)
