from copy import deepcopy  # In case you need it :)


def remove_min_and_max(a_list: list) -> None:
    """Removes the lowest number and the highest number from the list."""

    raise NotImplementedError  # TODO: Implement the function.


def without_outliers(a_list: list) -> list:
    """Returns a copy of the given list, with the lowest and highest numbers excluded."""

    raise NotImplementedError  # TODO: Implement the function.


# Feel free to make use of the following function in your implementations.
def find_min_and_max_index(a_list: list) -> tuple:
    """Finds the position of the lowest number and the highest number in the list."""

    min_index, max_index = 0, 0

    for i in range(1, len(a_list)):
        if a_list[i] < a_list[min_index]:
            min_index = i

        if a_list[i] > a_list[max_index]:
            max_index = i

    return min_index, max_index


""" 
# Alternatively:
def find_min_and_max_index(a_list: list) -> tuple:
    min_index = a_list.index(min(a_list))
    max_index = a_list.index(max(a_list))
    return min_index, max_index
 """
