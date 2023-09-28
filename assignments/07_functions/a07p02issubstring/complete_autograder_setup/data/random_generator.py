#!/usr/bin/python3
import random
import sys

from string import ascii_letters


def main():
    random.seed(sys.argv[-1])

    desired_outcome = sys.argv[1]
    assert desired_outcome in ("match", "nomatch")
    min_n = int(sys.argv[2])
    max_n = int(sys.argv[3])
    assert min_n <= max_n

    full_string = random_string(min_n, max_n)

    if desired_outcome == "match":
        length_of_substring = random.randint(1, len(full_string) - 1)
        max_start = len(full_string) - length_of_substring
        start = random.randint(0, max_start)
        stop = start + length_of_substring
        substring = full_string[start:stop]
        print(substring)
        print(full_string)

    else:
        assert desired_outcome == "nomatch"

        random_sub = random_string(min_n, max_n)
        while random_sub in full_string:
            random_sub += random.choice(ascii_letters)

        print(random_sub)
        print(full_string)


def random_string(min_n, max_n):
    n = random.randint(min_n, max_n)
    return "".join(random.choices(ascii_letters, k=n))


if __name__ == "__main__":
    main()
