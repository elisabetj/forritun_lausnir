def find_index_of_kth_occurrence(
    sequence: str, element_to_find: str, occurrence: int
) -> int:
    """Returns the location of the k-th occurrence of an element within a sequence."""

    seen_so_far = 0
    for index, element in enumerate(sequence):
        if element == element_to_find:
            seen_so_far += 1
            if seen_so_far == occurrence:
                return index


if __name__ == "__main__":
    print(find_index_of_kth_occurrence(input(), input(), int(input())))
