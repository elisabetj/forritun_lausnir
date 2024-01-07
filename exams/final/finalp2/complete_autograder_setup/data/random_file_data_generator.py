#!/usr/bin/python3

import random
import sys

MAX_THROWS = 4


def main():
    filename_prefix = sys.argv[1]
    filename_number = int(sys.argv[2])
    filename = f"{filename_prefix}{str(filename_number)}.txt"
    random.seed(filename_number)
    max_lines = int(sys.argv[3])
    more_than_one_throw_for_competitor = bool(int(sys.argv[4]))

    file_object = open("throwers.txt", "r")
    names_list = get_data(file_object)
    num_lines = random.randint(1, max_lines)
    write_data(filename, names_list, num_lines, more_than_one_throw_for_competitor)


def get_data(file_object):
    """Returns a list of names found in the given file_oject."""
    name_list = []
    for line in file_object:
        name = line.strip("\n")
        name_list.append(name)

    return name_list


def write_data(filename, names_list, num_lines, more_than_one_throw_for_competitor):
    """Writes random data into the given filename.
    Make sure that four throws at the maximum are generated for each name."""
    num_names_in_file = len(names_list)
    count_dict = {}
    with open(filename, "w+") as f:
        count = 0
        while count < num_lines:
            idx = random.randint(0, num_names_in_file - 1)
            name = names_list[idx]

            try:
                if more_than_one_throw_for_competitor:
                    if count_dict[name] == MAX_THROWS:
                        continue
                    else:
                        count_dict[name] += 1
                else:
                    if count_dict[name] == 1:
                        continue
            except KeyError:
                count_dict[name] = 1

            f.write(name + " ")
            throw = random.randint(5000, 7500) / 100
            f.write(str(throw) + "\n")
            count += 1


if __name__ == "__main__":
    main()
