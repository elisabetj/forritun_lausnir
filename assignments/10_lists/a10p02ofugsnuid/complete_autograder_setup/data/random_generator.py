#!/usr/bin/env pypy

from __future__ import print_function
from __future__ import division
import subprocess
import random
import math
import sys
import string

min_n = int(sys.argv[1]) # upper bound
max_n = int(sys.argv[2])
random.seed(int(sys.argv[3]))

n = random.randint(min_n, max_n)
print(n)
for x in range(n):
    print(random.randint(1,10**9))

#print('%s' % line)
#sys.stderr.write("wrote N={}\n".format(len(line)))
