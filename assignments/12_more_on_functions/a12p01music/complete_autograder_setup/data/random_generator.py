#!/usr/bin/python3
import random
import sys

from string import ascii_letters

whitespace = " \t"
letters_and_whitespace = ascii_letters + whitespace

random.seed(sys.argv[-1])

MIN_LENGTH = int(sys.argv[1])
MAX_LENGTH = int(sys.argv[2])
assert MIN_LENGTH >= 1


def main():
    music = random_preference()
    band = random_preference()
    singer = random_preference()

    print(music, band, singer, sep=",")


def random_preference():
    if included():
        return random_string()
    else:
        return random_whitespace()


def included() -> bool:
    coin_toss = random.randint(0, 1)
    return coin_toss == 1


def random_string():
    n = random.randint(MIN_LENGTH, MAX_LENGTH)
    prefix_length = random.randrange(n)
    postfix_length = n - 1 - prefix_length

    prefix = random.choices(letters_and_whitespace, k=prefix_length)
    at_least_one_character = random.choice(ascii_letters)
    postfix = random.choices(letters_and_whitespace, k=postfix_length)

    return "".join(prefix + [at_least_one_character] + postfix)


def random_whitespace():
    n = random.randint(0, 5)
    return "".join(random.choices(whitespace, k=n))


if __name__ == "__main__":
    main()
