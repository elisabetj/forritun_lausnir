#!/usr/bin/python3

MAX_GUESS = 12
CHAR_PLACEHOLDER = "-"


def main():
    """Reads seed and words from a file and starts the game."""

    file_name = input()
    file_object = open_file(file_name)
    word_index = int(input())
    if file_object is not None:
        word_list = get_words(file_object)
        file_object.close()
        secret_word = word_list[word_index - 1]
        guess_word = initialize_guess_word(secret_word)
        play(secret_word, guess_word)


def open_file(filename):
    """Opens the given file, returning its file object if found, otherwise None."""

    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return None


def get_words(file_object):
    """Returns a list of words found in in the given file_oject."""

    word_list = []
    for word in file_object:
        word_list.append(word.strip())

    return word_list


def initialize_guess_word(secret_word):
    """Returns a list, whose length is equal to the length of the secret word,
    and for which each element is initalized with the character placeholder."""

    guess_word = [CHAR_PLACEHOLDER] * len(secret_word)
    return guess_word


def play(secret_word, guess_word):
    """Runs the play loop."""

    num_guesses = 0
    print_current_guess_word(guess_word)

    while num_guesses < MAX_GUESS:
        guess = input().lower()
        num_guesses += 1
        print(f"Guess {num_guesses}/{MAX_GUESS}")
        process_guess(guess, secret_word, guess_word)
        print_current_guess_word(guess_word)
        if not CHAR_PLACEHOLDER in guess_word:
            print("You won!")
            break
    else:
        print(f"You lost! The secret word was {secret_word}")


def print_current_guess_word(guess_word):
    print("Secret word: {}".format(" ".join(guess_word)))


def process_guess(guess, secret_word, guess_word):
    """Updates the letters in the guess word. Furthermore, prints out appropriate messages."""

    if guess in secret_word:
        print(f"Correct letter {guess}!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guess_word[i] = guess
    else:
        print(f"Incorrect letter {guess}!")


if __name__ == "__main__":
    main()
