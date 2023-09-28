def extract_first_number_from_string(string_to_search: str) -> int:
    number_string = ""
    digits_spotted = False
    for character in string_to_search:
        if character.isdigit():
            number_string += character
            digits_spotted = True
        elif digits_spotted:
            # If we have already seen a digit,
            # but the current character is not,
            # then we have seen the entire first number.
            break

    if digits_spotted:
        return int(number_string)
    else:
        return -1


if __name__ == "__main__":
    string_to_search = input()
    print(extract_first_number_from_string(string_to_search))
