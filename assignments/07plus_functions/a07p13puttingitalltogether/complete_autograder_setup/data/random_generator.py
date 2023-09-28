#!/usr/bin/python3
import sys
import random
from itertools import permutations as pm

random.seed(sys.argv[-1])

discs = int(sys.argv[1])
from_pillar = 1
to_pillar = 3 

state = ''.join([str(x) for x in range(discs,0,-1)])
state += "|||"

print(discs)
print(from_pillar)
print(to_pillar)
print(state)


