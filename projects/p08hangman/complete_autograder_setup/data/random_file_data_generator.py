#!/usr/bin/python3

import random
import sys

def get_data(file_object):
    '''Returns a list of words found in the given file_oject.''' 
    
    word_list = []
    for line in file_object:
        word = line.strip()
        word_list.append(word)
    
    return word_list


filename_number = int(sys.argv[1])
filename = "test"+str(filename_number)+".txt"
random.seed(filename_number)
num_words_to_pick = int(sys.argv[2])

file_object = open("english_nouns.txt", 'r')
word_list = get_data(file_object)
num_words_in_file = len(word_list)

with open(filename, 'w+') as f:
    for i in range(num_words_to_pick):
        idx = random.randint(0, num_words_in_file - 1)
        f.write(word_list[idx] + "\n")
