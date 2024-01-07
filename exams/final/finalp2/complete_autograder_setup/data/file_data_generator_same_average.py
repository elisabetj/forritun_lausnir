#!/usr/bin/python3

import sys

MAX_THROWS = 4

# Three sequences of throws with the same average:
NAMES = ["John Smith", "Robby Jones", "Paul Gerard"]
THROWS1 = [52, 58, 70]
THROWS2 = [54, 60, 66]
THROWS3 = [56, 50, 74]


def main():
    filename_prefix = sys.argv[1]
    filename_number = int(sys.argv[2])
    filename = f"{filename_prefix}{str(filename_number)}.txt"

    generate_data(filename)


def write_data(f, name, throws_list):
    """Writes data to f for name using throws_list."""
    for i in range(len(throws_list)):
        f.write(name + " ")
        throw = throws_list[i]
        f.write(str(throw) + "\n")


def generate_data(filename):
    """Generates data for three players into the given filename.
    Make sure that the average throw is equal."""
    throws = [THROWS1, THROWS2, THROWS3]

    with open(filename, "w+") as f:
        for i in range(3):
            name = NAMES[i]
            write_data(f, name, throws[i])


if __name__ == "__main__":
    main()
