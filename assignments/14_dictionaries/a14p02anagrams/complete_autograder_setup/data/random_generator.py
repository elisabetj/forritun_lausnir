#!/usr/bin/python3
import random
import sys
from string import punctuation, ascii_lowercase
import math
from typing import List


random.seed(sys.argv[-1])
char_pool = ascii_lowercase
ANAGRAM = sys.argv[1] == "true"
STRING_LENGTH = int(sys.argv[2])
UPPERCASE = sys.argv[3] == "upper"  # if true add upper case to pool
PUNCTUATION = (
    sys.argv[4] == "punc"
)  # add punctuation to pool test correct handeling of punctuatuion


def are_anagrams(sentence_1: str, sentence_2: str) -> bool:
    return string_to_dict(sentence_1) == string_to_dict(sentence_2)


def string_to_dict(string):
    string_dict = {}
    for letter in string:
        if letter not in punctuation + " ":
            add_letter_to_dict(letter.lower(), string_dict)
    return string_dict


def add_letter_to_dict(letter, string_dict):
    if letter not in string_dict:
        string_dict[letter] = 0

    string_dict[letter] += 1


def random_string() -> str:
    return "".join(random.choices(char_pool, k=STRING_LENGTH))


def main() -> None:
    sentence_1 = random_string()
    sentence_2 = random_string()

    if PUNCTUATION:  # adds random punctiation
        for _ in range(math.ceil(STRING_LENGTH / 3)):
            sentence_2 += "".join(random.choice(punctuation + " "))

        for _ in range(math.ceil(STRING_LENGTH / 3)):
            sentence_1 += "".join(random.choice(punctuation + " "))

    if not ANAGRAM:
        while are_anagrams(sentence_1=sentence_1, sentence_2=sentence_2):
            sentence_2 = random_string()
    else:
        sentence_2 = sentence_1[:]

        sentence_2_list = list(sentence_2)

        if UPPERCASE:  # add random uppercase to sentance 2
            for index in random.choices(
                range(STRING_LENGTH), k=math.ceil(STRING_LENGTH / 4)
            ):
                sentence_2_list[index] = sentence_2_list[index].upper()

        random.shuffle(sentence_2_list)
        sentence_2 = "".join(sentence_2_list)

    print(sentence_1)
    print(sentence_2)


if __name__ == "__main__":
    main()
