#!/usr/bin/python3
import random
import sys
from string import ascii_letters

random.seed(sys.argv[-1])

test_type = sys.argv[1]


def main():
    assert test_type in [
        "__init__",
        "__str__",
        "guess_letter",
    ], f"Invalid test type {test_type}."
    print(test_type)

    print(random_hangman_word())


def random_hangman_word():
    word_len = random.randint(5, 20)
    return "".join(random.choices(ascii_letters, k=word_len))


if __name__ == "__main__":
    main()
