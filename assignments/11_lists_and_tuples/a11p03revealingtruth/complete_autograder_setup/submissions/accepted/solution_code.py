from typing import List, Tuple


def main():
    a_list = get_input()
    a_tuple = list_to_bool_tuple(a_list)
    print(a_tuple)


def get_input() -> List[str]:
    return input().strip().split(",")


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


if __name__ == "__main__":
    main()
