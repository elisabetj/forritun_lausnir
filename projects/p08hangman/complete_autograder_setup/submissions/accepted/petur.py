#!/usr/bin/python3
from typing import List

MAX_GUESSES = 12
UNREVEALED_CHARACTER = "-"


def main():
    word = get_word()
    if word is not None:
        play_hangman(secret_word=word)


def get_word() -> str | None:
    """Picks a word from a file, as specified by the user."""
    words = read_words_from_file()
    if words:
        return select_word(words)


def read_words_from_file() -> List[str] | None:
    """Asks the user for a file name and returns the words found in the specified file."""
    file_name = input()
    try:
        with open(file_name) as file:
            return extract_words(file)
    except FileNotFoundError:
        return None


def extract_words(file) -> List[str]:
    """Returns a list of words found in in a file with one word per line."""
    return [line.strip() for line in file]


def select_word(words: List[str]) -> str:
    """Asks the user which word to pick from the list, and returns the chosen word."""
    word_number = int(input())
    index = word_number - 1
    assert 0 <= index < len(words)
    return words[index]


def play_hangman(secret_word: str) -> None:
    attempt: list = initialize_attempt(secret_word)
    guess_number = 1
    while guess_number <= MAX_GUESSES and unfinished(attempt):
        print(f"Guess {guess_number}/{MAX_GUESSES}")
        take_a_guess(attempt, secret_word)
        guess_number += 1

    declare_outcome(attempt, secret_word)


def initialize_attempt(secret_word):
    """Hides the characters in the secret word.

    Returns a list, whose length is equal to the length of the secret word,
    and for which each element is initalized with a placeholder.
    """
    attempt = [UNREVEALED_CHARACTER] * len(secret_word)
    show_progress(attempt)
    return attempt


def take_a_guess(attempt_so_far: List[str], secret_word: str) -> None:
    """Asks the player for a guess, and responds to the guess."""
    new_guess = input()
    respond(new_guess, secret_word)
    update_attempt(new_guess, attempt_so_far, secret_word)
    show_progress(attempt_so_far)


def respond(guess: str, secret_word: str) -> None:
    if guess_is_correct(guess, secret_word):
        print(f"Correct letter {guess}!")
    else:
        print(f"Incorrect letter {guess}!")


def guess_is_correct(guess: str, secret_word: str) -> bool:
    return guess.lower() in secret_word.lower()


def update_attempt(guess: str, attempt: List[str], secret_word: str) -> None:
    """Reveals any hidden letters corresponding to the guess."""
    for index, character in enumerate(secret_word):
        if guess.lower() == character.lower():
            attempt[index] = character


def show_progress(attempt: List[str]) -> None:
    print(f"Secret word: {' '.join(attempt)}")


def declare_outcome(attempt: List[str], secret_word: str) -> None:
    if unfinished(attempt):
        print(f"You lost! The secret word was {secret_word}")
    else:
        print("You won!")


def unfinished(attempted: List[str]) -> bool:
    return UNREVEALED_CHARACTER in attempted


if __name__ == "__main__":
    main()
