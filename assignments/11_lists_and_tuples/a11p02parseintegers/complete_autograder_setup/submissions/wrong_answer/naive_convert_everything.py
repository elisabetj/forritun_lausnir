def main():
    raw_list = input().strip().split(",")
    final_tuple = list_to_int_tuple(raw_list)
    print(final_tuple)


def list_to_int_tuple(mixed_list: list) -> tuple:
    try:
        return tuple([int(element) for element in mixed_list])
    except ValueError:
        return tuple(mixed_list)

if __name__ == "__main__":
    main()
