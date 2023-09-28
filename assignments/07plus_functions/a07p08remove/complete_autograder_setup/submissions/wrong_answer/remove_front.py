from typing import Tuple

def remove_at(sequence: str, index_to_remove: int) -> Tuple[str, str]:
    """Removes an element from a sequence at the specified index.

    Returns the updated sequence and the element that was removed, in that order.
    """
    removed_element = sequence[0]
    updated_sequence = sequence[:0] + sequence[0 + 1 :]
    return updated_sequence, removed_element


if __name__ == "__main__":
    print(remove_at(input(), int(input())))
