#!/usr/bin/python3

def main():
    file_name = input()
    file_stream = open_file(file_name)
    if file_stream is not None:
        word_list = get_words(file_stream)
        print_info(word_list)
        token_list = get_tokens(word_list)
        print_info(token_list)
        file_stream.close()
   

def open_file(filename):
    '''Returns a file stream if filename found, otherwise None.'''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None


def get_words(file_stream):
    '''Returns a list the words found in the given stream.'''

    all_words = []
    for line in file_stream:
        word_list = line.strip().split()
        for word in word_list:
            all_words.append(word)
    
    return all_words

def print_info(a_list):
    '''Prints information about a_list.'''

    print(len(a_list))
    print_list(a_list)


def print_list(a_list):
    '''Prints the tokens in the given list, one in each line.'''

    for token in a_list:
        print(token)


def get_tokens(word_list):
    '''Returns a tokenized version of word_list.
        , . ! ? are considered separate tokens when appearing at the end
        of a word.'''

    return word_list


def print_list(token_list):
    '''Prints the tokens in the given list, one in each line.'''

    for token in token_list:
        print(token)


if __name__ == "__main__":
    main()