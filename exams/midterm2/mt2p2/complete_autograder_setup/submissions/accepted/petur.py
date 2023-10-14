from typing import List

PUNCTUATION_SYMBOLS = ",.?!"


def main() -> None:
    file_handle = get_file()
    if file_handle is None:
        return

    with file_handle:
        words = extract_words(file_handle)

    tokens = get_tokens(words)

    display_output(words, tokens)


def get_file():
    file_name = input()
    try:
        return open(file_name)
    except FileNotFoundError:
        return None


def extract_words(file) -> List[str]:
    words = []
    for line in file:
        words.extend(line.split())

    return words


def get_tokens(words: List[str]) -> List[str]:
    tokens = []
    for word in words:
        if word[-1] in PUNCTUATION_SYMBOLS:
            actual_word = word[:-1]
            punctuation = word[-1]
            tokens.extend([actual_word, punctuation])
        else:
            tokens.append(word)

    return tokens


def display_output(words: List[str], tokens: List[str]) -> None:
    for output_list in words, tokens:
        display_items(output_list)


def display_items(items: List[str]) -> None:
    print(len(items))
    for item in items:
        print(item)


if __name__ == "__main__":
    main()
