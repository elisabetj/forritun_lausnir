#!/usr/bin/python3

import random
import sys
import string

DIGIT = 0
LETTER = 1

random.seed(sys.argv[-1])
max_number_of_tokens = int(sys.argv[1])
max_length_of_token = int(sys.argv[2])

num_tokens = random.randint(1, max_number_of_tokens)
SYMBOLS = string.digits + string.ascii_letters
# 40 times more likely selecting a digit compared to selecting a letter
WEIGHTS = [40] * len(string.digits) + [1] * len(string.ascii_letters)

def random_token(max_length_of_token):
    len_token = random.randint(1, max_length_of_token)
    return ''.join(random.choices(SYMBOLS, weights=WEIGHTS, k=len_token))
    
token_string = ' '.join(random_token(max_length_of_token) for _ in range(num_tokens))
print(token_string)
