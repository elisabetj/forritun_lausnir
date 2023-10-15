import sys


def main():
    lines = sys.stdin.readlines()
    for line in lines:
        assert line.endswith('\n') and not line.endswith('\n\n')
    lines = [line.rstrip('\n') for line in lines]
    assert len(lines) == 1
    line = lines[0]

    set_of_functions = set(["tan", "sleep", "randint", "enumerate", "namedtuple", "cos", "print", "sum", "important_function1", "new_line"])
    assert line in set_of_functions, f"{repr(line)} is not one of the functions"


    exit(42)


if __name__ == "__main__":
    main()
