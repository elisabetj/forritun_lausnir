#!/usr/bin/python3

def main():
    line = input()
    string_list = line.split()
    print(string_list)
    int_list = get_ints(string_list)
    print(int_list)
    missing_int_list = get_missing_ints(int_list)
    print(missing_int_list)


def get_ints(string_list):
    '''Returns a list of the integers found in string_list.'''

    int_list = []
    for a_str in string_list:
        try:
            an_int = int(a_str)
            int_list.append(an_int)
        except ValueError:
            pass

    return int_list


def get_missing_ints(int_list):
    '''Returns a list of missing integers i from int_list, where 1 <= i < n and n is the maximum element in int_list.'''

    missing_ints = []
    if int_list:
        max_int = max(int_list)
        for i in range(max_int):
            if i not in int_list:
                missing_ints.append(i)

    return missing_ints


if __name__ == "__main__":
    main()