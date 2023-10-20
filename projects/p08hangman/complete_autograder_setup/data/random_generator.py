#!/usr/bin/python3

import sys
import random
import string

WIN = 0
LOSS = 1

def get_data(file_object):
    '''Returns a list of words found in the given file_oject.''' 
    
    word_list = []
    for line in file_object:
        word = line.strip()
        word_list.append(word)
    
    return word_list


def generate_win(secret_word):
    '''Generates winning solution using characters from the secret word.
    Also add some characters not in the secret word.'''

    CORRECT = 0
    INCORRECT = 1

    letters_set = set(secret_word)
    num_letters = len(secret_word)
    counter = 0

    for ch in letters_set:
        print(ch)
        counter += secret_word.count(ch)

        mode = random.choices([CORRECT, INCORRECT],[0.6, 0.4])[0]
        if counter < num_letters and mode == INCORRECT:
            ch = random.choice(string.ascii_lowercase)
            if not ch in secret_word:
                print(ch)


def generate_loss(secret_word):
    '''Generates a loss given the secret word.'''

    for i in range(12): # 12 tries
        ch = random.choice(string.ascii_lowercase)
        print(ch)


filename_number = int(sys.argv[1])
max_words_in_file = int(sys.argv[2])

random.seed(filename_number)
idx = random.randint(1, max_words_in_file)
file_name = "test"+str(filename_number)+".txt"

file_object = open(file_name, 'r')
word_list = get_data(file_object)
secret_word = word_list[idx - 1]

print(file_name)
print(idx)

if filename_number <= 20:
    kind = random.choice([WIN, LOSS])
    if kind == WIN:
        generate_win(secret_word)
    else:
        generate_loss(secret_word)