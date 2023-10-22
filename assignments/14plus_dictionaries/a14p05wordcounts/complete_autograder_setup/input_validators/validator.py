import sys

REQUIRED_NUMBER_OF_LINES = 1
MAX_LENGTH = 100


def main():
    lines = sys.stdin.readlines()
    lines = [line.rstrip() for line in lines]
    assert len(lines) >= REQUIRED_NUMBER_OF_LINES
    assert all([1 <= len(file_name) <= MAX_LENGTH for file_name in lines])
    assert any(file_name.endswith(".txt") for file_name in lines)

    exit(42)


if __name__ == "__main__":
    main()
