def is_substring_of(potential_substring: str, potential_superstring: str) -> bool:
    # The potential_substring doesn not necessarily have to appear
    # at the beginning of the longer string,
    # it can be anywhere inside it, so this does not work,
    # as this only checks for prefix.
    for index in range(len(potential_superstring)):
        if index < len(potential_substring) and (
            potential_substring[index] != potential_superstring[index]
        ):
            return False

    return True
