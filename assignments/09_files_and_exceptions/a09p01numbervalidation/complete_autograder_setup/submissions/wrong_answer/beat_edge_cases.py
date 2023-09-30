INT_CHARS = "0123456789"
DECIMAL_CHARS = INT_CHARS + "."


def is_float(string_to_test: str) -> bool:
    number_of_dots = string_to_test.count(".")
    number_of_es = string_to_test.count("e")

    if string_to_test and number_of_dots <= 1:
        if string_to_test in ["inf", "-inf", "NaN"]:
            return True
        elif string_to_test in ["."]:
            return False
        elif number_of_es == 0:
            return all(x in DECIMAL_CHARS for x in string_to_test)
        elif number_of_es == 1:
            base, exponent = string_to_test.split("e")
            base_valid = all(x in DECIMAL_CHARS for x in base)
            exponent_valid = all(x in INT_CHARS for x in exponent)
            return base_valid and exponent_valid
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    potential_number = input()
    return_value = is_float(potential_number)
    print(return_value)
