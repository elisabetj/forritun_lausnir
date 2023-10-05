from typing import List, Tuple


def list_to_bool_tuple(a_list: List[str]) -> Tuple[bool]:
    """Returns a tuple with each element in the list converted to bool.

    First converts any integers to int.
    """
    bool_list = []
    for item in a_list:
        bool_item = discover_the_truth(item)
        bool_list.append(bool_item)

    return tuple(bool_list)


def discover_the_truth(source: str) -> bool:
    try:
        truth = bool(int(source))
    except ValueError:
        truth = bool(source)

    return truth
