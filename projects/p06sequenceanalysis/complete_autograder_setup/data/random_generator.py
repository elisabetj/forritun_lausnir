#!/usr/bin/python3

import random
import sys
import string

VALID_NUM = 0
INVALID_NUM = 1

filename_number = int(sys.argv[1])
max_numbers_in_seq = int(sys.argv[2])
filename = "test"+str(filename_number)+".txt"
random.seed(filename_number)

numbers_in_seq = random.randint(1, max_numbers_in_seq)
# generate either a valid float string or a string which is likely an invalid float
with open(filename, 'w+') as f:
    for i in range(numbers_in_seq):
        choice_list = random.choices([VALID_NUM, INVALID_NUM], [0.9, 0.1])
        if choice_list[0] == VALID_NUM:
            number = random.uniform(-20, 20)
            f.write(str(number)+"\n")
        else:
            res = ''.join(random.choices(string.ascii_letters +
                             string.digits, k=5))
            f.write(res+"\n")