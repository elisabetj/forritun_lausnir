#!/usr/bin/python3
DIGITS = 2


def main():
    filename = input()
    file_object = open_file(filename)
    if file_object is not None:
        process_file(file_object)
        file_object.close()


def open_file(filename):
    """Opens the given file, returning its file object if found, otherwise None"""

    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return None


def process_file(file_object):
    """Processes the data given the file object."""

    input_data_tuple_list = get_data(file_object)
    print_tuples(input_data_tuple_list)
    first_last_tuple_list = get_first_last_in_year(input_data_tuple_list)
    print_tuples(first_last_tuple_list)
    inflation_tuple_list = calc_inflation(first_last_tuple_list)
    print_tuples(inflation_tuple_list)


def get_data(file_object):
    """Returns a list of tuples found in each line in the given file_oject.
    Each tuple is of the form (year_month, index)"""

    tuple_list = []
    for line in file_object:
        year_month_str, index_str = line.split()
        tuple_list.append((year_month_str, float(index_str)))
    return tuple_list


def print_tuples(tuple_list):
    """Prints the contents of tuple_list, each tuple in a separate line."""

    for a_tuple in tuple_list:
        print(a_tuple)


def get_first_last_in_year(tuple_list):
    """Returns a list of tuples where each tuple is of the form (year, index_for_first_month, index_for_last_month)."""

    return_tuple_list = []
    previous_year = 0

    if tuple_list:  # Get the first index for the first year
        (year_month_str, first_index_for_year) = tuple_list[0]

    for a_tuple in tuple_list:
        (year_month_str, index) = a_tuple
        year = int(year_month_str[0:4])  # year_month_str is, for examle, '1990M01'
        if previous_year != 0 and year != previous_year:
            last_index_for_year = previous_index
            return_tuple_list.append(
                (previous_year, first_index_for_year, last_index_for_year)
            )
            first_index_for_year = index

        previous_year = year
        previous_index = index

    # The case for the last index for the last year
    last_index_for_year = previous_index
    return_tuple_list.append((previous_year, first_index_for_year, last_index_for_year))

    return return_tuple_list


def calc_inflation(first_last_tuple_list):
    """Returns a tuple with the calculated inflation for each year based on the input data
    which consist of a list of tuples where each tuple is of the form
    (year, first_index_for_year, last_index_for_year)."""

    inflation_tuple_list = []
    for a_tuple in first_last_tuple_list:
        year = a_tuple[0]
        last_index = a_tuple[2]
        first_index = a_tuple[1]

        inflation = 100 * ((last_index / first_index) - 1)
        inflation_tuple_list.append((year, round(inflation, DIGITS)))

    return inflation_tuple_list


if __name__ == "__main__":
    main()
