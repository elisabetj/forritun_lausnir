def find_index_of_nth_occurrence(
    sequence: str, element_to_find: str, occurrence: int
) -> int:
    """Returns the location of the n-th occurrence of an element within a sequence."""

    seen_so_far = 0
    for index, element in enumerate(sequence):
        if element == element_to_find:
            seen_so_far += 1
            if seen_so_far == occurrence:
                return index
    return -1


def insert_at(sequence: str, index: int, element: str) -> str:
    """Inserts an element at the specified location in a sequence and returns the updated sequence."""

    return sequence[:index] + element + sequence[index:]


def put_on_pillar(state: str, disc: str, pillar: int) -> str:
    """Puts the given disc on the specified pillar.

    Returns the updated state.
    """

    where_to_insert = find_index_of_nth_occurrence(
        sequence=state,
        element_to_find="|",
        occurrence=pillar,
    )

    new_state = insert_at(
        sequence=state,
        index=where_to_insert,
        element=disc,
    )

    return new_state


if __name__ == "__main__":
    print(put_on_pillar(input(), input(), int(input())))
