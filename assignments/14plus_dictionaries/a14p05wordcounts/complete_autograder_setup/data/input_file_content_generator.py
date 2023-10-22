#!/usr/bin/python3
import random
import sys
from string import ascii_letters
from typing import List, Dict

random.seed(sys.argv[-1])


def main():
    word_counts = select_word_counts()
    words = generate_words(word_counts)
    lines = divide_words_into_lines(words)
    print_lines(lines)


def select_word_counts(max_frequency: int = 20) -> Dict[int, int]:
    return {
        frequency: choose_count(frequency) for frequency in range(1, max_frequency + 1)
    }


def choose_count(frequency: int) -> int:
    return random.randrange(max_count_for_frequency(frequency))


def max_count_for_frequency(frequency: int) -> int:
    return 50 // frequency


def generate_words(word_counts: Dict[int, int]) -> List[str]:
    """Creates a random list of words with the requested frequency distribution."""
    number_of_words = sum(word_counts.values())
    unique_words = random_words(number_of_words)
    assert len(unique_words) == number_of_words

    words = []
    for frequency, count in word_counts.items():
        unique_words_of_this_frequency = unique_words[:count]
        unique_words = unique_words[count:]
        assert len(unique_words_of_this_frequency) == count

        words_of_this_frequency = []
        for word in unique_words_of_this_frequency:
            words_of_this_frequency.extend([word] * frequency)

        assert len(words_of_this_frequency) == frequency * count
        assert len(set(words_of_this_frequency)) == count

        words.extend(words_of_this_frequency)

    assert unique_words == []

    random.shuffle(words)

    assert len(set(words)) == number_of_words
    assert len(words) >= number_of_words
    assert len(words) == sum(
        [frequency * count for frequency, count in word_counts.items()]
    )
    assert satisfies_distribution(words, word_counts)
    return words


def random_words(number_of_words: int) -> List[str]:
    """Creates a list of distinct words, as many as requested."""
    words = [random_word() for _ in range(number_of_words)]
    words = list(set(words))

    while len(words) < number_of_words:
        word = random_word()
        while word in words:
            word += random_word()

        words.append(word)

    assert len(set(words)) == len(words)  # All distinct.
    return words


def random_word() -> str:
    length = random.randrange(1, 10)
    return "".join(random.choices(ascii_letters, k=length))


def satisfies_distribution(words: List[str], word_counts: Dict[int, int]) -> bool:
    positive_word_counts = {
        frequency: count for frequency, count in word_counts.items() if count > 0
    }
    return count_by_frequency(words) == positive_word_counts


def count_by_frequency(words: List[str]) -> dict:
    """Counts words of each frequency.

    All words that appear exactly once are counted,
    all words that appear exactly twice are counted, etc.

    Returns a dictionary, where
        the keys are the frequencies,
            how often a particular word occurs,
        and the values are the counts,
            the number of words that appear with that frequency.
    """
    word_frequencies = count_each_word(words)

    frequency_counts = {}

    for frequency in word_frequencies.values():
        if frequency not in frequency_counts:
            frequency_counts[frequency] = 0

        frequency_counts[frequency] += 1

    return frequency_counts


def count_each_word(words: List[str]) -> dict:
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


def divide_words_into_lines(
    words: List[str],
    min_words_per_line: int = 2,
) -> List[List[str]]:
    number_of_words = len(words)
    assert min_words_per_line <= number_of_words

    max_lines = number_of_words // min_words_per_line
    assert max_lines * min_words_per_line <= number_of_words

    min_lines = min(3, max_lines)
    assert min_lines <= max_lines

    number_of_lines = random.randint(min_lines, max_lines)
    assert number_of_lines * min_words_per_line <= number_of_words

    lines = []
    for _ in range(number_of_lines):
        line = words[:min_words_per_line]
        words = words[min_words_per_line:]
        lines.append(line)
    assert all(len(line) == min_words_per_line for line in lines)

    for word in words:
        line = random.choice(lines)
        line.append(word)
    assert all(len(line) >= min_words_per_line for line in lines)

    assert sum(len(line) for line in lines) == number_of_words
    return lines


def print_lines(lines: List[List[str]]) -> None:
    for line in lines:
        print(" ".join(line))


if __name__ == "__main__":
    main()
