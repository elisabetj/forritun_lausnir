#!/usr/bin/python3
import random
import sys
from string import ascii_letters

random.seed(sys.argv[-1])  # Using the first argument for seeding.


def main():
    number_of_lines = random.randrange(100)
    for _ in range(number_of_lines):
        print(random_line())


def random_line():
    number_of_words = random.randrange(20)
    words = [random_word_or_number() for _ in range(number_of_words)]
    return " ".join(words)


def random_word_or_number():
    if random.randint(0, 3):
        return random_word()
    else:
        return str(random.randrange(10000))


def random_word():
    length = random.randrange(1, 10)
    return "".join(random.choices(ascii_letters, k=length))


if __name__ == "__main__":
    main()
