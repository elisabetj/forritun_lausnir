import sys


def main():
    lines = sys.stdin.readlines()
    lines = [line.rstrip() for line in lines]
    assert len(lines) == 1
    line = lines[0]

    numbers = [int(i) for i in line.split()]
    assert 1 <= len(numbers) <= 1000
    assert all(1 <= number < 100 for number in numbers)

    exit(42)


if __name__ == "__main__":
    main()
