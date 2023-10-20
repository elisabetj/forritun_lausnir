#!/usr/bin/python3
import sys
import re

MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'


def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None.'''
  
  try:
    file_object = open(filename, 'r')
    return file_object
  
  except FileNotFoundError:
    return None
  

def get_words(file_object):
    '''Returns a list of words found in in the given file_oject.''' 
    
    word_list = []
    for word in file_object:
        word_list.append(word.strip())
    
    return word_list


def initialize_guess_word(secret_word):
    '''Returns a list, whose length is equal to the length of the secret word,
    and for which each element is initalized with the character placeholder.'''

    guess_word = [CHAR_PLACEHOLDER] * len(secret_word)
    return guess_word


def process_guess(guess, secret_word, guess_word):
    '''Updates the letters in the guess word.'''

    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            guess_word[i] = guess
    

def play(secret_word, guess_word):
    '''Runs the play loop.'''

    num_guesses = 0
    
    while CHAR_PLACEHOLDER in guess_word and num_guesses < MAX_GUESS:
        guess_str = sys.stdin.readline() # the file name
        assert re.match('[a-z]\n$', guess_str), 'Illegal character guess'
        guess = guess_str.strip()
        num_guesses += 1
        process_guess(guess, secret_word, guess_word)
        

file_name = sys.stdin.readline() # the file name
assert re.match('[a-zA-Z0-9_-]+[.]{1}txt\n$', file_name), 'Illegal name of file'
file_name = file_name.strip()
file_name = "./p08hangman/data/" + file_name

word_index_str = sys.stdin.readline()
assert re.match('[1-9][0-9]?\n$', word_index_str), 'Format of word index incorrect'
word_index = int(word_index_str.strip())
assert word_index >= 1 and word_index <= 20, 'Index of word not in range'

file_object = open_file(file_name)
if file_object is not None:
    word_list = get_words(file_object)
    secret_word = word_list[word_index - 1]
    guess_word = initialize_guess_word(secret_word)
    play(secret_word, guess_word)
    file_object.close()

assert not sys.stdin.read()
sys.exit(42)
