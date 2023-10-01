#!/usr/bin/python3
import random
import sys
from string import digits

random.seed(sys.argv[-1])

min_len = int(sys.argv[1])
max_len = int(sys.argv[2])
differing_sizes = bool(int(sys.argv[3]))

a_len = 10**random.randint(min_len, max_len)
b_len = a_len
if differing_sizes:
	# rejection sampling
	while a_len == b_len:
		b_len = 10**random.randint(min_len, max_len)

# jebb = random.randrange(2)
# if jebb and not differing_sizes:
# 	a = random.choices(digits, k = a_len)
# 	b = random.sample(a, k = b_len) # as per the python docs
# else:
# 	# rejection sampling
# 	while True:
# 		a = random.choices(digits, k = a_len)
# 		b = random.choices(digits, k = b_len)
# 		if sorted(a) != sorted(b):
# 			break

def perm(a, b):
	return sorted(str(a)) == sorted(str(b))

neibb = random.randrange(2) | differing_sizes
while True:
	a = random.randrange(a_len // 10, a_len)
	b = random.randrange(b_len // 10, b_len)
	if perm(a, b) != neibb:
		break


print(str(a))
print(str(b))
