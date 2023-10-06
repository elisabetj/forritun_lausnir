import sys


def main():
    lines = sys.stdin.readlines()
    lines = [line.rstrip() for line in lines]
    assert len(lines) >= 1

    assert all(len(line) >= 1 for line in lines)
    assert any(line.endswith(".txt") for line in lines)

    exit(42)


if __name__ == "__main__":
    main()
