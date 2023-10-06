#!/usr/bin/python3

import random
import sys

from string import ascii_letters, digits
alphanumeric = ascii_letters + digits

QUIT = 'q'
COLLECT_DIGITS = 'c'
INVERSE_CASE = 'i'
TO_HEX = 'h'

random.seed(sys.argv[-1])
max_num_input = int(sys.argv[1])

num_input_examples = random.randint(1, max_num_input)
for i in range(num_input_examples):
    choice_list = random.choices([COLLECT_DIGITS, INVERSE_CASE, TO_HEX, QUIT], [30, 30, 30, 10])
    choice = choice_list[0]
    print(choice)
    if choice == QUIT:
        break
    elif choice == TO_HEX:
        the_string = str(random.randint(0, 99999))
    else:
        num_letters = random.randint(1, 20)
        the_string = ''.join(random.choices(population=alphanumeric, k=num_letters))
    print(the_string)
else:
    print(QUIT)
