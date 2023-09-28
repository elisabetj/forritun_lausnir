# Use recursion to solve the Tower of Hanoi puzzle
# The objective is to get n discs, stacked on the first pillar, over to the third pillar.
# To do so:
# - we first get the n-1 discs over to the second pillar (via recursion)
# - then we can move the one remaining (and largest) disc from the first pillar to the third pillar
# - finally we get the n-1 discs from the second pillar to the third pillar (via recursion)
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


def insert_at(sequence: str, index: int, element: str) -> str:
    """Inserts an element at the specified location in a sequence and returns the updated sequence."""

    return sequence[:index] + element + sequence[index:]


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


def put_on_pillar(state: str, disc: str, pillar: int) -> str:
    """Puts the given disc on the specified pillar.

    Returns the updated state.
    """

    where_to_insert = find_index_of_nth_occurrence(
        sequence=state, element_to_find="|", occurrence=pillar
    )

    new_state = insert_at(sequence=state, index=where_to_insert, element=disc)

    return new_state


def move_one(from_pillar: int, to_pillar: int, old_state: str) -> str:
    """Moves the topmost disc from one pillar to another and returns the updated state representation."""

    intermediate_state, disc_being_moved = take_from_pillar(
        state=old_state, pillar=from_pillar
    )

    new_state = put_on_pillar(
        state=intermediate_state, disc=disc_being_moved, pillar=to_pillar
    )

    return new_state


def move_many(
    number_of_discs: int, from_pillar: int, to_pillar: int, state: str
) -> str:
    """Moves the specified number of discs from one pillar to another and returns the updated state representation.

    Prints the state for every move made.
    """

    if number_of_discs > 0:
        auxiliary_pillar = 6 - from_pillar - to_pillar
        state = move_many(number_of_discs - 1, from_pillar, auxiliary_pillar, state)
        state = move_one(from_pillar, to_pillar, state)
        print(state)
        state = move_many(number_of_discs - 1, auxiliary_pillar, to_pillar, state)
    return state


if __name__ == "__main__":
    number_of_discs = int(input())
    from_pillar = int(input())
    to_pillar = int(input())
    #   initial_state = ""
    #   for disc in range(number_of_discs, 0, -1):
    #       initial_state += str(disc)
    #   initial_state += "|||"
    initial_state = input()
    move_many(number_of_discs, from_pillar, to_pillar, initial_state)
