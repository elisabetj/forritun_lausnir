import sys
import random
import string

random.seed(sys.argv[-1])

MIN_UNIQUE = int(sys.argv[1])
MAX_UNIQUE = int(sys.argv[2])
assert 1 <= MIN_UNIQUE <= MAX_UNIQUE
NUMBER_OF_UNIQUE_WORDS = random.randint(MIN_UNIQUE, MAX_UNIQUE)

MIN_REPS = int(sys.argv[3])
MAX_REPS = int(sys.argv[4])
assert 0 <= MIN_REPS <= MAX_REPS
NUMBER_OF_REPETITIONS = random.randint(MIN_REPS, MAX_REPS)

NUMBER_OF_INSERTIONS = NUMBER_OF_UNIQUE_WORDS + NUMBER_OF_REPETITIONS
assert 1 <= NUMBER_OF_INSERTIONS <= 30

SORTED = "sorted"
RANDOM = "random"
test_category = sys.argv[5]
assert test_category in (SORTED, RANDOM)

VALID_CHARACTERS = string.ascii_letters + string.digits
MAX_WORD_LENGTH = 10
MAX_DEFINITION_LENGTH = 70

YES = "y"
NO = "n"


def main():
    words = generate_words()
    for i, word in enumerate(words):
        print(word)
        print(make_random_definition())
        print(NO if i == NUMBER_OF_INSERTIONS - 1 else YES)


def generate_words() -> list:
    words = generate_unique_words()
    mix_in_repetitions(words)
    assert len(words) == NUMBER_OF_INSERTIONS
    return words


def generate_unique_words(number_of_words=NUMBER_OF_UNIQUE_WORDS) -> list:
    words = [make_random_word() for _ in range(number_of_words)]
    words = list(set(words))

    MAX_ATTEMPTS = 3
    attempts = 0
    while len(set(words)) < number_of_words:
        word = make_random_word()
        if word not in words:
            words.append(word)

        assert attempts < MAX_ATTEMPTS
        attempts += 1

    assert len(set(words)) == len(words)
    return words


def mix_in_repetitions(words: list) -> None:
    repetitions = random.choices(words, k=NUMBER_OF_REPETITIONS)
    words.extend(repetitions)
    if test_category == SORTED:
        words.sort()
    else:
        assert test_category == RANDOM
        random.shuffle(words)


def make_random_word() -> str:
    length = random.randint(1, MAX_WORD_LENGTH)
    return "".join(random.choices(VALID_CHARACTERS, k=length))


def make_random_definition() -> str:
    length = 0
    words = []
    word = make_random_word()
    while length + len(word) <= MAX_DEFINITION_LENGTH:
        length += len(word)
        words.append(word)
        word = make_random_word()

    return " ".join(words)


if __name__ == "__main__":
    main()
