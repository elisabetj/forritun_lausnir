import sys

min_insetrions = 1
max_insertions = 30


def main():
    lines = sys.stdin.readlines()
    for line in lines:
        assert line.endswith("\n") and not line.endswith("\n\n")
    lines = [line.rstrip("\n") for line in lines]
    assert 3 * min_insetrions <= len(lines) <= 3 * max_insertions

    for line in lines[2::3]:
        assert line.lower() == "y" or line.lower() == "n"

    exit(42)


if __name__ == "__main__":
    main()
