#!/usr/bin/env python3

EXIT = "x"


def main():
    first_word = get_word()
    # The first word is always valid.
    valid = [first_word]
    invalid = []

    while (word := get_word()) != EXIT:
        if word_is_valid(word, valid):
            valid.append(word)
        else:
            invalid.append(word)

    display_words(valid)
    display_words(invalid)


def get_word() -> str:
    return input().lower()


def word_is_valid(new_word: str, previous_words: list) -> bool:
    last_valid_word = previous_words[-1]
    return new_word[0] == last_valid_word[-1]


def display_words(words: list) -> None:
    print(" ".join(words))


if __name__ == "__main__":
    main()
