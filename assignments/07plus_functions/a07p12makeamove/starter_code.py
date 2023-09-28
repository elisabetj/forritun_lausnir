from typing import Tuple

def find_index_of_nth_occurrence(
    sequence: str, element_to_find: str, occurrence: int
) -> int:
    """Returns the location of the n-th occurrence of an element within a sequence."""

    # ... add your code


def remove_at(sequence: str, index_to_remove: int) -> Tuple[str, str]:
    """Removes an element from a sequence at the specified index.

    Returns the updated sequence and the element that was removed, in that order.
    """

    # ... add your code


def insert_at(sequence: str, index: int, element: str) -> str:
    """Inserts an element at the specified location in a sequence and returns the updated sequence."""

    # ... add your code


def take_from_pillar(state: str, pillar: int) -> Tuple[str, str]:
    """Removes the top disc from the specified pillar.

    Returns the updated state and the disc that was removed, in that order.
    """

    # ... add your code


def put_on_pillar(state: str, disc: str, pillar: int) -> str:
    """Puts the given disc on the specified pillar.

    Returns the updated state.
    """

    # ... add your code


def move_one(from_pillar: int, to_pillar: int, old_state: str) -> str:
    """Moves the topmost disc from one pillar to another and returns the updated state representation."""

    # ... implement this method, utilizing the functions defined above
