def main():
    input_list = get_correct_data()

    sorted_list = sorted(input_list)
    unique_list = unique_elements(sorted_list)
    composite_list = composite_elements(unique_list)
    print_lists(input_list, sorted_list, composite_list)

    min_int, max_int, average = calculate_statistics(input_list)
    print_stats(min_int, max_int, average)


def get_correct_data() -> list:
    """Asks user repeatedly for input until valid."""

    input_list = get_data()
    while input_list is None:
        input_list = get_data()

    return input_list


def get_data():
    """Returns a list of positive integers input by the user.

    Returns None if the input contains non-integers or integers < 0.
    """

    raw_list = input().split(",")

    try:
        int_list = [int(element) for element in raw_list]
    except ValueError:
        return None

    for number in int_list:
        if number <= 0:
            return None

    return int_list


def unique_elements(a_list: list) -> list:
    """Returns a new list containing the unique elements in a_list."""

    result = []
    for element in a_list:
        if not element in result:
            result.append(element)
    return result


def composite_elements(a_list: list) -> list:
    """Returns a new list containing the composite numbers in a_list."""

    return [number for number in a_list if is_prime(number)]


def is_prime(n: int) -> bool:
    """Returns True if the given positive number is prime and False otherwise."""

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def print_lists(input_list: list, sorted_list: list, composite_list: list) -> None:
    """Prints the given lists."""

    print(f"Input list: {input_list}")
    print(f"Sorted list: {sorted_list}")
    print(f"Composite list: {composite_list}")


def calculate_statistics(int_list: list) -> tuple:
    """Returns statistics from the given list: min, max and average."""

    max_int = max(int_list)
    min_int = min(int_list)
    average = sum(int_list) / len(int_list) if int_list else 0
    return min_int, max_int, average


def print_stats(min_int: int, max_int: int, average: float) -> None:
    """Prints the statistics."""

    print(f"Min: {min_int:d}, Max: {max_int:d}, Average: {average:.2f}")


if __name__ == "__main__":
    main()
