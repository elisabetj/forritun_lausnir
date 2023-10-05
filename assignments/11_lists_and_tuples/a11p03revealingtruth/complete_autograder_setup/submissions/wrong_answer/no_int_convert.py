from typing import List, Tuple


def main():
    a_list = get_input()
    a_tuple = list_to_bool_tuple(a_list)
    print(a_tuple)


def get_input() -> List[str]:
    return input().strip().split(",")


def list_to_bool_tuple(a_list: list) -> Tuple[bool]:
    bool_list = []
    for item in a_list:
        bool_item = discover_the_truth(item)
        bool_list.append(bool_item)

    return tuple(bool_list)


def discover_the_truth(source) -> bool:
    truth = bool(source)
    return truth


if __name__ == "__main__":
    main()
