#!/usr/bin/env python3


def main():
    length, collection = read_input()

    ordered_sequence = order_collection(collection=collection)
    assert len(ordered_sequence) == length

    star_wars_ordered_sequence = prioritize_middle(
        length=length,
        sequence=ordered_sequence,
    )

    display_result(star_wars_ordered_sequence)


def read_input() -> tuple[int, list[str]]:
    length = int(input())
    assert length % 3 == 0

    collection = input().split()
    assert len(collection) == length

    return length, collection


def order_collection(collection: list[str]) -> list[str]:
    """Sorts the numbers in the list, as numbers, not alphabetically."""
    int_collection = []
    for string in collection:
        int_collection.append(int(string))

    ordered_sequence = sorted(int_collection)

    string_sequence = []
    for number in ordered_sequence:
        string_sequence.append(str(number))

    return string_sequence


def prioritize_middle(length: int, sequence: list[str]) -> list[str]:
    assert len(sequence) == length

    first = length // 3
    second = 2 * first
    third = length
    assert third == 3 * first

    original = sequence[first:second]
    prequels = sequence[0:first]
    sequels = sequence[second:third]
    star_wars_ordered_sequence = original + prequels + sequels

    return star_wars_ordered_sequence


def display_result(sequence: list[str]) -> None:
    print(" ".join(sequence))


if __name__ == "__main__":
    main()
