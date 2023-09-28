#!/usr/bin/python3
import sys
import random
from itertools import permutations as pm


pillar = int(sys.argv[1])
long = int(sys.argv[2])
c = int(sys.argv[3])
offset = pillar * 10 + c
if long:
    options =list(set([''.join(x)+'|' for x in pm("54321||")]))
    case = random.randint(0,len(options)-1)
    case = options[case]
else:
    options =list(set([''.join(x)+'|' for x in pm("321||")]))
    case = options[offset]


pos = -1
free_disc = case.index('|')
while pos < 0:
    if free_disc > 0 and case[free_disc-1] != '|':
        pos = free_disc-1
    else:
        free_disc = case.index('|',free_disc+1)
disc = case[pos]
new_case = case[:pos] + case[pos+1:]
print(new_case)
print(disc)
print(pillar)


