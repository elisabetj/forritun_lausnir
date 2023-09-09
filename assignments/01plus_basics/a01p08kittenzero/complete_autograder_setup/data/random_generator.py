#!/usr/bin/python3
import sys

#random.seed(sys.argv[-1])

x = int(sys.argv[1])
#max_x = int(sys.argv[2])

y = 2+(x/100)
print("{:.2f}".format(y))
