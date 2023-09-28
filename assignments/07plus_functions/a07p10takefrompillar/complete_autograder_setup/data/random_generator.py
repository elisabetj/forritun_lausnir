#!/usr/bin/python3
import sys
import random
from itertools import permutations as pm


pillar = int(sys.argv[1])

options =list(set([''.join(x)+'|' for x in pm("54321||")]))
if pillar == 1:
    options = [x for x in options if not x.startswith('|')]
else:
    options = [x for x in options if '||' not in x]

case = random.randint(0,len(options)-1)
print(options[case])
print(pillar)


