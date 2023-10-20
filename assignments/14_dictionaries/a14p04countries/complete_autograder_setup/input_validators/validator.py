import sys

REQUIRED_NUMBER_OF_LINES = 3
MAX_WRONG = 10
MAX_LENGTH = 100
MAX_QUERIES = 1000000
MAX_QUERY = 50

COUNTRIES = "countries.txt"
CORRECT = (COUNTRIES,)
YES = "y"
NO = "n"


def main():
    lines = sys.stdin.readlines()
    lines = [line.rstrip() for line in lines]
    assert len(lines) >= REQUIRED_NUMBER_OF_LINES
    assert any([line in CORRECT for line in lines])

    incorrect_file_names = []
    index = 0
    while lines[index] not in CORRECT:
        incorrect_file_names.append(lines[index])
        index += 1
    assert len(incorrect_file_names) <= MAX_WRONG
    for invalid in incorrect_file_names:
        assert len(invalid) <= MAX_LENGTH

    correct_file_name = lines[index]
    index += 1
    assert correct_file_name in CORRECT

    queries = lines[index:]
    assert len(queries) % 2 == 0
    number_of_queries = len(queries) // 2
    assert number_of_queries <= MAX_QUERIES

    for i in range(number_of_queries):
        query = queries[2 * i]
        assert query.isdigit() and 1 <= int(query) <= MAX_QUERY

        more = queries[2 * i + 1]
        assert more in (YES, NO)

        if i < number_of_queries - 1:
            assert more == YES
        else:
            assert i == number_of_queries - 1
            assert more == NO

    exit(42)


if __name__ == "__main__":
    main()
