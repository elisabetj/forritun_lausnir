#!/usr/bin/python3

import sys
import random

filename_number = int(sys.argv[1])
max_words_in_file = int(sys.argv[2])

random.seed(filename_number)
idx = random.randint(1, max_words_in_file)
file_name = "test"+str(filename_number)+".txt"

print(file_name)
print(idx)

