from typing import Tuple

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


def remove_at(sequence: str, index_to_remove: int) -> Tuple[str, str]:
    """Removes an element from a sequence at the specified index.

    Returns the updated sequence and the element that was removed, in that order.
    """

    removed_element = sequence[index_to_remove]
    updated_sequence = sequence[:index_to_remove] + sequence[index_to_remove + 1 :]
    return updated_sequence, removed_element


def take_from_pillar(state: str, pillar: int) -> Tuple[str, str]:
    """Removes the top disc from the specified pillar.

    Returns the updated state and the disc that was removed, in that order.
    """

    pillar_position = find_index_of_nth_occurrence(
        sequence=state, element_to_find="|", occurrence=pillar
    )
    position_of_top_disc = pillar_position - 1

    new_state, removed_disc = remove_at(
        sequence=state, index_to_remove=position_of_top_disc
    )

    return new_state, removed_disc


if __name__ == "__main__":
    print(take_from_pillar(input(), int(input())))
