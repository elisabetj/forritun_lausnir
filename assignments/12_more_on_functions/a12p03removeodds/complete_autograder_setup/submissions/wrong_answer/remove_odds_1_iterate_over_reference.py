from typing import List


def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""

    remove_odds_1(int_list)


def remove_odds_1(int_list: List[int]) -> None:
    """Attempts to remove odd integers from the given list.

    Makes a reference first.
    Iterates over the reference, and modifies the original.
    Unfortunately this also modifies the reference...
    """

    reference = create_a_reference(int_list)

    # We iterate over the reference
    # but unfortunately that does not stay unchanged
    # because it is a reference to the same object,
    # and will get modified accordingly.
    for num in reference:
        if num % 2 == 1:
            int_list.remove(num)


def create_a_reference(int_list: List[int]) -> List[int]:
    """Returns a reference to the given list, not a copy."""

    # A reference does not a copy make:
    reference = int_list
    # If we modify the reference, then we also modify the original.
    # And vice versa.

    return reference


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""

    return [number for number in int_list if number % 2 == 0]
