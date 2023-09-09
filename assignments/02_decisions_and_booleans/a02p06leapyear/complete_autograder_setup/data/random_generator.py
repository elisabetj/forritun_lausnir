#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

lower = int(sys.argv[1])
upper = int(sys.argv[2])
leapYearType = int(sys.argv[3])

year = random.randint(lower, upper)
if leapYearType == 1:
	year -= year % 4
	if year % 100:
		year += 4
elif leapYearType == 2:
	year -= year % 100
	if year % 400:
		year += 100
elif leapYearType == 3:
	year -= year % 400

print(year)
