from typing import List, Tuple


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


def remove_min_and_max(a_list: List[int]) -> None:
    """Removes the lowest number and the highest number from the list."""

    a_list.remove(min(a_list))
    a_list.remove(max(a_list))


def without_outliers(a: List[int]) -> List[int]:
    """Returns a copy of the given list, with the lowest and highest numbers excluded."""

    min_index, max_index = find_min_and_max_index(a)
    return [a[i] for i in range(len(a)) if (i != min_index and i != max_index)]


def find_min_and_max_index(a_list: List[int]) -> Tuple[int]:
    """Finds the position of the lowest number and the highest number in the list."""

    min_index = a_list.index(min(a_list))
    max_index = a_list.index(max(a_list))
    return min_index, max_index


if __name__ == "__main__":
    main()
