from solution_code import find_index_of_kth_occurrence


def main():
    sequence = input()
    element_to_find = input()
    occurrence = int(input())
    return_val = find_index_of_kth_occurrence(sequence, element_to_find, occurrence)
    print(return_val)
    assert isinstance(return_val, int)


if __name__ == "__main__":
    main()
