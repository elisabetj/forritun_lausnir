#!/usr/bin/python3

import string

DOCUMENT_END = '<END OF DOCUMENT>'
SEARCH = 'search'
PRINT = 'print'
NO_MATCH = "No match"

def open_file(filename):
    '''Opens the given filname and returns its file object, or None if not found'''
    try:
        file_object = open(filename, 'r')
        return file_object
    except FileNotFoundError:
        return None


def get_docs_list(file_object):
    '''Reads all documents in the file_object into a list and returns it.
    Each list entry is a string representing a document.'''

    all_docs = []
    doc = ''
    for line in file_object:
        # Store all lines of each document in string 
        # which is then appended to all_docs when the end of a document is encountered
        if line.strip() == DOCUMENT_END: 
            all_docs.append(doc)
            doc = '' # start new document
        else:
            doc += line
    
    return all_docs
    

def build_dict(all_docs):
    '''Builds and returns a word dictionary for the given document list.
    The value of each word is a set of the document numbers the word appears in.'''
    word_dict = {}

    for idx, doc_str in enumerate(all_docs): 
        word_list = doc_str.split()
        for word in word_list:
            word = word.strip().lower().strip(string.punctuation)
            if word:
                if word in word_dict:
                    word_dict[word].add(idx)
                else:
                    word_dict[word] = {idx} # a set with one document number
    return word_dict


def print_document_numbers(document_set):
    '''Prints out document numbers, sorted in ascending order.''' 
    document_list = sorted(document_set)
    if document_list:
        print("Documents matching search: ", end = '')
        for i in document_list:
            print(i + 1, end = ' ')
        else:
            print()
    else:
        print(NO_MATCH)


def print_document(all_docs, doc_num):
    '''Prints out the contents of a particular document. doc_num is zero-based'''
    if doc_num > len(all_docs) or doc_num < 1:
        print(NO_MATCH)
    else:
        print("Document #{}:".format(doc_num))
        # There is a new line at the end of each document string.
        # Make sure we do not get an empty line in the output.
        print(all_docs[doc_num - 1], end = '')  


def execute_actions(all_docs, word_dict):
    action = input()
    while action in {SEARCH, PRINT}:
        if action == PRINT:
            doc_num = int(input())
            print_document(all_docs, doc_num)
        action = input()
   

def main():
    document_file = input()
    file_object = open_file(document_file)
    if file_object is not None:
        all_docs_list = get_docs_list(file_object)
        file_object.close()
        word_dict = build_dict(all_docs_list)
        execute_actions(all_docs_list, word_dict)


if __name__ == "__main__":
    main()
