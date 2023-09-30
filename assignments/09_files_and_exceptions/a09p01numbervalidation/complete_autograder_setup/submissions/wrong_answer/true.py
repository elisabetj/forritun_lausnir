def is_float(string_to_test: str) -> bool:
    return True


if __name__ == "__main__":
    potential_number = input()
    return_value = is_float(potential_number)
    print(return_value)
