#!/usr/bin/python3

import random
import sys

QUIT = 'q'

random.seed(sys.argv[-1])
max_num_passwords = int(sys.argv[1])
max_num_letters = int(sys.argv[2])

num_passwords = random.randint(1, max_num_passwords)
for i in range(1, num_passwords):
    passwd = ''
    num_letters = random.randint(1, max_num_letters)
    for c in range(1, num_letters + 1):
        num = random.randint(48, 122)    # a specific range in the ASCII table
        passwd += chr(num)
    print(passwd)
    if passwd == QUIT:
        break
else:
    print(QUIT)
