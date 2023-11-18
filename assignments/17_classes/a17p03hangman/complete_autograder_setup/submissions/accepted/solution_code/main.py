#!/usr/bin/python3

from hangman import Hangman


def main() -> None:
    requested_method = input()
    available_methods = {
        "__init__": create_hangword,
        "__str__": display_word,
        "guess_letter": guess_letter,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run()


def create_hangword():
    word = input()
    hangword = Hangman(word)
    print(f"Hangman word created from the word '{word}'.")
    return hangword


def display_word(hangword=None):
    if hangword is None:
        hangword = create_hangword()

    print(hangword)


def guess_letter(hangword=None):
    if hangword is None:
        hangword = create_hangword()

    print("Hangmand word before guess:")
    print(hangword)

    letter = "a"
    result = hangword.guess_letter(letter)

    print(f"Letter {letter} guessed.")
    print("Correctly." if result else "Incorrectly.")
    print("Hangmand word after guess:")
    print(hangword)


if __name__ == "__main__":
    main()
