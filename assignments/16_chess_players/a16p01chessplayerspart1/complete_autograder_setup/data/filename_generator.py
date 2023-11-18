#!/usr/bin/python3
import random
import sys
from string import ascii_letters


random.seed(sys.argv[-1])

filename_suffix = int(sys.argv[1])
filename = f"test_file_{filename_suffix:02d}.csv"


def main():
    print(filename)


if __name__ == "__main__":
    main()
