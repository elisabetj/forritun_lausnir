def is_substring_of(potential_substring: str, potential_superstring: str) -> bool:
    return potential_substring in potential_superstring


if __name__ == "__main__":
    potential_substring = input()
    search_string = input()
    print(is_substring_of(potential_substring, search_string))
