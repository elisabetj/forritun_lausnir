def is_substring_of(potential_substring: str, potential_superstring: str) -> bool:
    # The potential_substring can be anywhere inside the other string,
    # starting from any index in the longer string,
    # as long as there is still enough room for it behind that index.
    last_possible_starting_index = len(potential_superstring) - len(potential_substring)

    start_index = 0
    while start_index <= last_possible_starting_index:
        no_mismatch_found = True
        index = 0
        offset = start_index
        while index < len(potential_substring) and offset < len(potential_superstring):
            if potential_substring[index] != potential_superstring[offset]:
                no_mismatch_found = False

            index += 1
            offset += 1

        if no_mismatch_found:
            return True

        start_index += 1

    # This double loop is not the fastest method.
    # It can be made more efficient using state machines, which you'll learn about later.
    # Therefore, you're better off using the builtin string method rather than implementing this manually,
    # but it can be enlightening to peek under the hood.

    return False
