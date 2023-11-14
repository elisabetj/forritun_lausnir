#!/usr/bin/python3
import re
import string
import sys

SYMBOLS = string.ascii_letters + string.punctuation

SEARCH = 'search'
PRINT = 'print'
QUIT = 'quit'          

file_name = sys.stdin.readline() # the file name
assert re.match('[a-zA-Z0-9_-]+[.]{1}txt\n$', file_name), 'Illegal name of file'

action = sys.stdin.readline()
if action == '':
    sys.exit(42)
assert re.match('(search|print|quit)\n$', action), 'Unknown action'

action = action.strip()
while action != QUIT:
    if action == SEARCH:
        search_words = sys.stdin.readline()
        assert search_words.endswith('\n') and not search_words.endswith('\n\n')
        assert any(c not in string.whitespace for c in search_words)
        search_words = search_words.rstrip('\n').split(' ')
        assert 1 <= len(search_words) <= 3
        for search_word in search_words:
            assert all(x in SYMBOLS for x in search_word), f"Illegal search string {repr(search_word)}"
    elif action == PRINT:
        doc_num = sys.stdin.readline()
        assert re.match('(0|-?[1-9][0-9]*)\n$', doc_num)
    
    action = sys.stdin.readline()
    assert re.match('(search|print|quit)\n$', action), 'Unknown action'
    action = action.strip()

assert not sys.stdin.read()
sys.exit(42)
