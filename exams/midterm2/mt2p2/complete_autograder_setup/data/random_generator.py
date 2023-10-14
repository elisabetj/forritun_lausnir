#!/usr/bin/python3

import random
import sys
import string

LETTER = 0
PUNCT = 1

filename_number = int(sys.argv[1])
random.seed(filename_number)
filename = "test"+str(filename_number)+".txt"

max_num_lines = int(sys.argv[2])
max_num_tokens_in_line = int(sys.argv[3])
max_num_letters_in_token = int(sys.argv[4])

num_lines = random.randint(1, max_num_lines)
with open(filename, 'w+') as f:
    for _ in range(num_lines):
        num_tokens_in_line = random.randint(1, max_num_tokens_in_line)
        for _ in range(num_tokens_in_line):
            token = ''
            num_letters = random.randint(1, max_num_letters_in_token)
            for _ in range(num_letters):
                ch = random.choice(string.ascii_letters)
                token += ch
            letter_punct = random.choices([LETTER, PUNCT],[0.8, 0.2])[0]
            if letter_punct == PUNCT:
                token += random.choice([',','.','?','!'])
            f.write(token + ' ')
        f.write("\n")