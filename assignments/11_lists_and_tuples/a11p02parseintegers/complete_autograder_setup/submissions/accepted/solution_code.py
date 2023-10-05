from typing import Tuple

def main():
    raw_list = input().strip().split(",")
    final_tuple = list_to_int_tuple(raw_list)
    print(final_tuple)


def list_to_int_tuple(mixed_list: list) -> Tuple:
    int_list = []
    for item in mixed_list:
        try:
            int_item = int(item)
            int_list.append(int_item)
        except ValueError:
            continue

    return tuple(int_list)


if __name__ == "__main__":
    main()
