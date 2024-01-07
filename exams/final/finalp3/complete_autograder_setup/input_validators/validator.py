#!/usr/bin/python3
import re
import sys

HEIGHT = 'height'

def check_input_number():
    num = sys.stdin.readline()
    assert re.match('[0-9]+\n$', num), 'Illegal number'
    

def check_height():
    method = sys.stdin.readline()
    assert re.match('(__init__|__str__|__gt__|__add__|cm)\n$', method), 'Unknown method'
    method = method.strip()
    check_input_number()
    check_input_number()

    if method == '__gt__' or method == "__add__":
        check_input_number()
        check_input_number()
    
    

def main():
    module_name = sys.stdin.readline()
    assert re.match('(height)\n$', module_name), 'Unknown module'

    module_name = module_name.strip()
    if module_name == HEIGHT:
        check_height()

    assert not sys.stdin.read()
    sys.exit(42)


if __name__ == "__main__":
    main()
