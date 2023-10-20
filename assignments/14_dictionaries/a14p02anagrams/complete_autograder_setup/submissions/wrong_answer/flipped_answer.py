from string import punctuation


def main():
    sentence_1 = input()
    sentence_2 = input()

    if are_anagrams(sentence_1, sentence_2):
        print(f"{sentence_1} is an anagram of {sentence_2}.")
    else:
        print(f"{sentence_1} is not an anagram of {sentence_2}.")


def are_anagrams(sentence_1: str, sentence_2: str) -> bool:
    return string_to_dict(sentence_1) != string_to_dict(sentence_2)


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


if __name__ == "__main__":
    main()
