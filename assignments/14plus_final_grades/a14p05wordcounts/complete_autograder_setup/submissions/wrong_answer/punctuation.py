UI = False


def main():
    with get_valid_file() as file_object:
        words = get_word_list(file_object)

    word_frequencies = count_each_word(words)
    frequency_groups = categorize_by_frequency(word_frequencies)
    display_result(frequency_groups)


def get_valid_file():
    """Asks the user for a file name, repeatedly, until a valid name is given.

    Returns the corresponding file, opened in read mode.
    """

    prompt = "Name of file:\n" if UI else ""
    file_name = input(prompt)
    while (file_obj := open_file(file_name)) is None:
        print(f"File {file_name} not found!")
        file_name = input(prompt)

    return file_obj


def open_file(file_name: str):
    """Returns the given file, open, if it exists, but None otherwise."""

    try:
        return open(file_name, "r")
    except FileNotFoundError:
        return None


def get_word_list(file_object) -> list:
    """Returns a list of the words found in the file associated with the file object.

    The words are transformed to lower case but punctuation is NOT stripped off the end of the word.
    """

    word_list = []
    for line in file_object:
        for word in line.split():
            word_list.append(word.lower())

    return word_list


def count_each_word(words: list) -> dict:
    """Counts how often each word appears in the given word list.

    Returns a dictionary, where
        the keys are the words,
        and the corresponding value is the frequency,
            how often that word occurs in the list.
    """

    frequencies = {}

    for word in words:
        if word not in frequencies:
            frequencies[word] = 0

        frequencies[word] += 1

    return frequencies


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

    frequency_groups = {}

    for word, frequency in word_frequencies.items():
        if frequency not in frequency_groups:
            frequency_groups[frequency] = []

        frequency_groups[frequency].append(word)

    return frequency_groups


def display_result(frequencies: dict) -> None:
    """Prints the words of each count, most frequent first."""

    for frequency in sorted(frequencies, reverse=True):
        words = frequencies[frequency]
        how_often = f"{frequency} times" if frequency > 1 else "only once"
        if len(words) == 1:
            print(f"There's only 1 word that appears {how_often}:")
        else:
            print(f"There are {len(words)} words that appear {how_often}:")

        print(f" {', '.join(words)}")


if __name__ == "__main__":
    main()
