#!/usr/bin/python3

import sys
import re

# Inputs needed for each method
# "__init__": x,y,z
# "__str__" : x,y,z
# "__abs__" : x,y,z
# "__add__" : vector1, vector2
# "__sub__" : vector1, vector2
# "__eq__"  : vector1, vector2
# "__mul__" : vector1, vector2
# "__rmul__": scalar , vector
# "__repr__": x,y,z
# "__gt__"  : vector1, vector2
# "__ge__"  : vector1, vector2
# "__lt__"  : vector1, vector2
# "__le__"  : vector1, vector2
# "dot"     : vector1, vector2
# "cross"   : vector1,vector2


def main():
    lines = sys.stdin.readlines()
    clean_lines = [line.strip() for line in lines]

    test_type = clean_lines.pop(0)
    for line in clean_lines:
        assert re.search("[0-9]+(.[0-9]+)?", line)

    if test_type in [
        "__init__",
        "__str__",
        "__abs__",
        "__repr__",
    ]:
        how_many = int(clean_lines.pop(0))
        assert len(clean_lines) == how_many, "Missing test parameters"

    elif test_type in [
        "__mul__",
        "__rmul__",
    ]:
        how_many = int(clean_lines.pop(0))
        assert len(clean_lines) == how_many + 1, "Missing test parameters"

    elif test_type in [
        "__add__",
        "__sub__",
        "__eq__",
        "__gt__",
        "__ge__",
        "__lt__",
        "__le__",
        "dot",
        "cross",
    ]:
        first = int(clean_lines.pop(0))
        second = int(clean_lines.pop(first))
        assert len(clean_lines) == first + second, "Missing test parameters"

    else:
        assert False, f"Invalid test type '{test_type}'."

    exit(42)


if __name__ == "__main__":
    main()
