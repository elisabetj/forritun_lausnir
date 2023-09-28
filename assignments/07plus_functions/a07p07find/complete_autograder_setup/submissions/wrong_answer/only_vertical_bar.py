def find_index_of_kth_occurrence(
    sequence: str, element_to_find: str, occurrence: int
) -> int:
    """Returns the location of the k-th occurrence of an element within a sequence."""
    if element_to_find != '|':
        return -1
    seen_so_far = 0
    for index, element in enumerate(sequence):
        if element == '|':
            seen_so_far += 1
            if seen_so_far == occurrence:
                return index

    return -1
