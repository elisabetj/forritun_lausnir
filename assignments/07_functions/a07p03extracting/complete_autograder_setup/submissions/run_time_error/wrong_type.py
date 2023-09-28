def extract_first_number_from_string(string_to_search: str) -> int:
    number_string = ""
    digits_spotted = False
    for character in string_to_search:
        if character.isdigit():
            number_string += character
            digits_spotted = True
        elif digits_spotted:
            break

    if digits_spotted:
        return number_string  # We are forgetting to convert this to int.
    else:
        return -1
