#!/usr/bin/python3

import sys
import random
import string

DOCUMENT_END = '<END OF DOCUMENT>'
SEARCH = 'search'
PRINT = 'print'
QUIT = 'quit'

random.seed(int(sys.argv[-1]))
suffix = sys.argv[1]
min_iterations = int(sys.argv[2])
max_iterations = int(sys.argv[3])
min_keywords = int(sys.argv[4])
max_keywords = int(sys.argv[5])
charset = sys.argv[6]
print_option = sys.argv[7]

assert charset in ["lower_no_punctuation", "lower", "no_punctuation", "any"]
assert print_option in ["valid", "any"]

def get_docs_list(file_object):
    '''Reads all documents in the file_object into a list and returns it.
    Each list entry is a string representing a document.'''

    all_docs = []
    doc = []
    for line in file_object:
        # Store all lines of each document in string 
        # which is then appended to all_docs when the end of a document is encountered
        if line.strip() == DOCUMENT_END: 
            all_docs.append(''.join(doc))
            doc = [] # start new document
        else:
            doc.append(line)
    
    return all_docs


def build_document_word_dict(all_docs):
    '''Builds and returns a dictonary for which the key is a document number and the value is a set of words found in the corresponding document.'''
    document_dict = {}

    for idx, doc_str in enumerate(all_docs):
        word_list = doc_str.split()
        word_set = set()
        for word in word_list:
            word = word.strip().lower().strip(string.punctuation)
            if word:
                word_set.add(word)
        document_dict[idx] = word_set

    return document_dict


def generate_search(document_dict, num_words, word_list):
    words = ['']
    while not all(words):
        doc_num = random.randint(1, len(document_dict))
        words = [word.strip(string.punctuation) for word in random.choices(word_list, k=num_words)]
    print(SEARCH)
    print(' '.join(words))


def generate_print(docs_list, print_option):
    if print_option == "valid":
        doc_num = random.randint(1, len(docs_list))
    else:
        doc_num = random.randint(1 - len(docs_list), len(docs_list)*2)
    print(PRINT)
    print(doc_num)


def random_word(symbols):
    count = random.randint(1, 7)
    res = ''.join(random.choices(symbols, k=count))
    return res


def random_line(existing_words):
    count = random.randint(1, 20)
    res = ' '.join(random.choices(existing_words, k=count)) + '\n'
    return res


def random_doc(existing_words):
    count = random.randint(1, 50)
    lines = [random_line(existing_words) for _ in range(count)]
    lines.append(DOCUMENT_END + '\n')
    return lines


def write_doc(filename, existing_words):
    number_of_docs = random.randint(0, 5) + 10 * (max_keywords + 1)
    lines = []
    for i in range(number_of_docs):
        lines.extend(random_doc(existing_words))
    with open(filename, 'w') as f:
        f.writelines(lines)


iterations = random.randint(min_iterations, max_iterations)
symbols = [c for c in string.ascii_lowercase]
if charset in ["lower", "any"]:
    symbols.extend([c for c in string.punctuation])
if charset in ["no_punctuation", "any"]:
    symbols.extend([c for c in string.ascii_uppercase])

existing_words = [random_word(symbols) for _ in range(3_000)]

file_name = f"docs_{suffix}.txt"
write_doc(file_name, existing_words)

file_object = open(file_name, 'r')
docs_list = get_docs_list(file_object)
document_dict = build_document_word_dict(docs_list)

print(file_name)

for _ in range(iterations):
    num_words = random.randint(min_keywords, max_keywords)
    kind = PRINT if num_words == 0 else SEARCH
    if kind == SEARCH:
        generate_search(document_dict, num_words, existing_words)
    else:
        generate_print(docs_list, print_option)

print(QUIT)
