#!/usr/bin/python3
import re
import sys

CLOCK = 'clock'

def check_int(lo, hi):
    line = sys.stdin.readline()
    assert re.match("^(0|[1-9][0-9]*)\n$", line), repr(line)
    value = line.strip()
    assert lo <= int(value) <= hi, f"Integer {value} out of range ({lo}-{hi})"

def check_clock():
    use_default = sys.stdin.readline()
    assert use_default in ["True\n", "False\n"], "Invalid value for use_default"
    check_int(0, 23)
    check_int(0, 60)
    check_int(0, 60)
    

def check_test():
    method = sys.stdin.readline()
    assert re.match('^(__init__|__str__|str_update|add_clocks)\n$', method), 'Unknown method'
    method = method.strip()
    check_clock()

    if method == 'str_update':
        line = sys.stdin.readline()
        assert re.match("^([01][0-9]|2[0-3])[:][0-5][0-9][:][0-5][0-9]\n$", line), f"Invalid clock string {repr(line)}"
    elif method == 'add_clocks':
        check_clock()


def main():
    check_test()

    assert not sys.stdin.read()
    sys.exit(42)


if __name__ == "__main__":
    main()
