import string


def main():
    with get_valid_file() as file_object:
        words: list = get_word_list(file_object)

    word_frequencies: dict = count_each_word(words)
    frequency_groups: dict = categorize_by_frequency(word_frequencies)
    display_result(frequency_groups)


def get_valid_file():
    """Asks the user for a file name, repeatedly, until a valid name is given.

    Returns the corresponding file, opened in read mode.
    """

    raise NotImplementedError  # TODO: remove this line and implement the function.


def open_file(file_name: str):
    """Returns the given file, open, if it exists, but None otherwise."""

    raise NotImplementedError  # TODO: remove this line and implement the function.


def get_word_list(file_object) -> list:
    """Returns a list of the words found in the file associated with the file object.

    The words are transformed to lower case and punctuation is stripped off the end of the word.
    """

    raise NotImplementedError  # TODO: remove this line and implement the function.


def count_each_word(words: list) -> dict:
    """Counts how often each word appears in the given word list.

    Returns a dictionary, where
        the keys are the words,
        and the corresponding value is the frequency,
            how often that word occurs in the list.
    """

    raise NotImplementedError  # TODO: remove this line and implement the function.


def categorize_by_frequency(word_frequencies: dict) -> dict:
    """Groups words by their frequency.

    All words that appear exactly once are listed together,
    all words that appear exactly twice are listed together, etc.

    Returns a dictionary, where
        the keys are the frequencies,
            how often a particular word occurs,
        and the corresponding value is a list,
            of all words that appear with that frequency.
    """

    raise NotImplementedError  # TODO: remove this line and implement the function.


def display_result(frequencies: dict) -> None:
    """Prints the words of each count, most frequent first."""

    raise NotImplementedError  # TODO: remove this line and implement the function.


if __name__ == "__main__":
    main()
