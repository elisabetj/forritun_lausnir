from solution_code import remove_at


def main():
    sequence = input()
    index_to_remove = int(input())
    return_val = remove_at(sequence, index_to_remove)
    print(return_val)

    assert isinstance(return_val, tuple), "Function did not return tuple."
    assert len(return_val) == 2, "Function did not return tuple of size 2."
    assert isinstance(
        return_val[0], str
    ), "First element of returned tuple is not a string."
    assert isinstance(
        return_val[1], str
    ), "Second element of returned tuple is not a string."


if __name__ == "__main__":
    main()
