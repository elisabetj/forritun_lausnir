STOP = "n"


def main():
    dictionary = {}

    add_word(dictionary)
    while more():
        add_word(dictionary)

    display_result(dictionary)


def add_word(dictionary: dict) -> None:
    """Asks the user for a word and definition and stores it in the dictionary."""

    word = input()
    dictionary[word] = input()


def more() -> bool:
    """Checks if the user wants to add more words."""

    answer = input()
    return answer.lower() != STOP


def display_result(dictionary: dict) -> None:
    """Prints the words in alphabetical order, along with the definitions."""

    for word, definition in dictionary.items():
        print(f"\n{word}:\n    {definition}")


if __name__ == "__main__":
    main()
