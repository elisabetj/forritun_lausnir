import sys

MAX_STRING_LEN = 70
NR_OF_LINES = 2


def main():
    lines = sys.stdin.readlines()
    for line in lines:
        assert line.endswith("\n") and not line.endswith("\n\n")
    lines = [line.rstrip("\n") for line in lines]
    assert len(lines) == NR_OF_LINES
    assert len(line[0]) <= MAX_STRING_LEN
    assert len(line[1]) <= MAX_STRING_LEN
    exit(42)


if __name__ == "__main__":
    main()
