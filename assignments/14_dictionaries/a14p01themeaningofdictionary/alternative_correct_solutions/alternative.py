STOP = "n"


def main():
    dictionary = {}

    add_word(dictionary)
    while more():
        add_word(dictionary)

    display_result(dictionary)


def add_word(dictionary: dict, user_interface: bool = False) -> None:
    """Asks the user for a word and definition and stores it in the dictionary."""

    if user_interface:
        word = input("Enter a word: ")
        dictionary[word] = input(f"Enter the definition for {word}: ")
    else:
        word = input()
        dictionary[word] = input()


def more(user_interface: bool = False) -> bool:
    """Checks if the user wants to add more words."""

    if user_interface:
        answer = input("Would you like to add another word and definition (y/n)?: ")
    else:
        answer = input()

    return answer.lower() != STOP


def display_result(dictionary: dict) -> None:
    """Prints the words in alphabetical order, along with the definitions."""

    for word in sorted(dictionary):
        definition = dictionary[word]
        print(f"\n{word}:\n    {definition}")


if __name__ == "__main__":
    main()
