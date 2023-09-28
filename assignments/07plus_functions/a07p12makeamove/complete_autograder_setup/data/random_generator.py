#!/usr/bin/python3
import sys
import random
from itertools import permutations as pm

random.seed(sys.argv[-1])

from_pillar = int(sys.argv[1])
to_pillar = int(sys.argv[2])

options =list(set([''.join(x)+'|' for x in pm("54321||")]))
casenr = random.randint(0,len(options)-1)
case = options[casenr]

fp= False 
count = 1
pillar_index = case.index('|')
while not fp:
    if (pillar_index == 0 and from_pillar == 1) or count > 3:
        casenr = (casenr +1) % (len(options)-1)
        case = options[casenr]
        pillar_index = case.index('|')
        count = 1

    if from_pillar != count:
        count+=1
        pillar_index = case.index('|',pillar_index+1)
    elif pillar_index > 0 and case[pillar_index-1] != '|':
        fp = True
    else:
        casenr = (casenr +1) % (len(options)-1)
        case = options[casenr]
        pillar_index = case.index('|')
        count = 1

print(from_pillar)
print(to_pillar)
print(case)


