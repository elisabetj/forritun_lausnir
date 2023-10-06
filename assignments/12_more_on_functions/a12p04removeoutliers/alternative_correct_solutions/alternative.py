from copy import deepcopy


def main():
    int_list = [int(string) for string in input().split()]
    print(f"Original list before calling functions: {int_list}")
    result = without_outliers(int_list)
    print(f"Resulting list after extracting middle: {result}")
    print(
        "Original list after extracting middle",
        f"and before removing outliers: {int_list}",
    )
    remove_min_and_max(int_list)
    print(f"Original list after removing outliers: {int_list}")


def remove_min_and_max(a_list: list) -> None:
    """Removes the lowest number and the highest number from the list."""

    min_index, max_index = find_min_and_max_index(a_list)

    a_list.pop(min_index)

    if min_index < max_index:
        max_index -= 1

    a_list.pop(max_index)


def without_outliers(a_list: list) -> list:
    """Returns a copy of the given list, with the lowest and highest numbers excluded."""

    new_list = deepcopy(a_list)
    remove_min_and_max(new_list)
    return new_list


def find_min_and_max_index(a_list: list) -> tuple:
    """Finds the position of the lowest number and the highest number in the list."""
    min_index, max_index = 0, 0

    for i in range(1, len(a_list)):
        if a_list[i] < a_list[min_index]:
            min_index = i

        if a_list[i] > a_list[max_index]:
            max_index = i

    return min_index, max_index


if __name__ == "__main__":
    main()
