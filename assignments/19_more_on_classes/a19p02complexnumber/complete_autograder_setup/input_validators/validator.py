import sys
import re

# Inputs needed for each method
# "__init__"   : [re, [im]]
# "__str__"    : C
# "__repr__"   : C
# "re"         : C
# "im"         : C
# "__eq__"     : CxC
# "conjugate"  : C
# "__neg__"    : C
# "__add__"    : CxC
# "__sub__"    : CxC
# "__mul__"    : CxC
# "inverse"    : C
# "__truediv__": CxC


def main():
    lines = sys.stdin.readlines()
    clean_lines = [line.strip() for line in lines]

    test_type = clean_lines.pop(0)
    for line in clean_lines:
        assert re.search("[0-9]+(.[0-9]+)?", line)

    if test_type in [
        "__init__",
        "__str__",
        "__repr__",
        "re",
        "im",
        "conjugate",
        "__neg__",
        "inverse",
    ]:
        how_many = int(clean_lines.pop(0))
        assert len(clean_lines) == how_many, "Missing test parameters"

    elif test_type in [
        "__eq__",
        "__add__",
        "__sub__",
        "__mul__",
        "__truediv__",
    ]:
        first = int(clean_lines.pop(0))
        second = int(clean_lines.pop(first))
        assert len(clean_lines) == first + second, "Missing test parameters"

    else:
        assert False, f"Invalid test type '{test_type}'."

    exit(42)


if __name__ == "__main__":
    main()
