import sys

MAX_LENGTH_OF_LINE = 30


def main():
    lines = sys.stdin.readlines()
    assert len(lines) >= 1

    last_line = lines[-1]
    assert last_line.strip()

    for line in lines:
        assert len(line) <= MAX_LENGTH_OF_LINE
        assert line.endswith("\n") and not line.endswith("\n\n")
        line = line.rstrip("\n")
        assert line == line.rstrip()
        if line.isnumeric() and line.startswith("0"):
            assert line == "0"

    exit(42)


if __name__ == "__main__":
    main()
