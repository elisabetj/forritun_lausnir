from string import punctuation


INTERSECTION_MESSAGE = "The two files have {} words in common."
UNIQUE_WORDS_MESSAGE = "There are {} words that are only in either file but not both."
EXCLUSIVE_MESSAGE = "There are {} words that only appear in the first file."


def main():
    filename1 = input()
    filename2 = input()

    words1 = read_words(filename1)
    words2 = read_words(filename2)

    shared_words = get_intersection(words1, words2)
    print_metric(shared_words, INTERSECTION_MESSAGE)

    unique_words = get_symmetric_difference(words1, words2)
    print_metric(unique_words, UNIQUE_WORDS_MESSAGE)

    exclusive_words = get_difference(words1, words2)
    print_metric(exclusive_words, EXCLUSIVE_MESSAGE)


def read_words(filename: str) -> set:
    """Returns the set of all words in the file, stripped of punctuation."""

    words_set = set()
    with open(filename) as file:
        for line in file:
            for word in line.split():
                words_set.add(word.strip(punctuation))

    return words_set


def get_intersection(set1: set, set2: set) -> set:
    """Returns the set of elements belonging to both the given sets."""

    return set1.intersection(set2)


def get_symmetric_difference(set1: set, set2: set) -> set:
    """Returns the set of elements belonging to one of the given sets, but not both."""

    return set1.symmetric_difference(set2)


def get_difference(set1: set, set2: set) -> set:
    """Returns the set of elements belonging to the first set and only the first set."""

    return set1 - set2


def print_metric(words: set, message: str) -> None:
    """States the number of words in the given set, and lists them, if any."""

    print()
    print(message.format(len(words)))
    word_list = list(words)
    if len(words) > 0:
        print("These words are as follows:")
        if len(words) > 1:
            print(f"{', '.join(word_list[:-1])} and {word_list[-1]}.")
        else:
            print(words.pop())


if __name__ == "__main__":
    main()
