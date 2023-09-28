def extract_first_number_from_string(string_to_search: str) -> int:
    number_string = ""
    digits_spotted = False
    for character in string_to_search:
        if character.isdigit():
            number_string += character
            # We are forgetting to record the fact that we have seen a digit already.
        elif digits_spotted:
            break

    if digits_spotted:
        return int(number_string)
    else:
        return -1
