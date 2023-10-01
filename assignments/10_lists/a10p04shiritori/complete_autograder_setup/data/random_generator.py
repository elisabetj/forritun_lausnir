#!/usr/bin/python3
import random
import sys
from string import ascii_letters as letters

random.seed(sys.argv[-1])

max_word_len = 100
min_len = int(sys.argv[1])
max_len = int(sys.argv[2])
error = float(sys.argv[3])

length = random.randrange(min_len, max_len)

last_word = ''.join(random.choices(letters, k = random.randrange(1, max_word_len)))
print(last_word)

for _ in range(length - 1):
	word = ''.join(random.choices(letters, k = random.randrange(1, max_word_len)))
	if random.random() > error:
		word = last_word[-1] + word
	if word == 'x':
		# in case we get unlucky
		word += ''.join(random.choices(letters, k = random.randrange(1, max_word_len)))
	last_word = word
	print(word)

print('x')
