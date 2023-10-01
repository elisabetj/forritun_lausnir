from operator import itemgetter


def main():
    names_and_ages = gather_all_inputs()
    show_oldest_and_youngest_persons(names_and_ages)
    show_central_tendency_measures(names_and_ages)


def gather_all_inputs() -> list:
    number_of_people = ask_for_number_of_people()
    names_and_ages = gather_names_and_ages(number_of_people)
    return names_and_ages


def ask_for_number_of_people() -> int:
    return ask_for_integer("")


def ask_for_integer(text: str) -> int:
    reply: str = input(text)
    while not is_integer(reply):
        print(f"{reply} is not an integer.")
        reply = input(text)

    return int(reply)


def is_integer(string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False


def gather_names_and_ages(how_many: int) -> list:
    names_and_ages: list = []
    for i in range(1, how_many + 1):
        name: str = input(f"{i}:")
        age: int = ask_for_integer(f"{i}:")
        names_and_ages.append([name, age])
    return names_and_ages


def show_oldest_and_youngest_persons(names_and_ages: list):
    oldest_person, max_age = find_oldest_person(names_and_ages)
    print(f"{oldest_person} ,{max_age}")
    youngest_person, min_age = find_youngest_person(names_and_ages)
    print(f"{youngest_person} ,{min_age}")


def find_oldest_person(names_and_ages: list):
    name, age = max(names_and_ages, key=itemgetter(1))
    return name, age


def find_youngest_person(names_and_ages: list):
    name, age = min(names_and_ages, key=itemgetter(1))
    return name, age


def show_central_tendency_measures(names_and_ages: list):
    PRECISION = 2
    median_age = determine_median_age(names_and_ages)
    print(f"{round(median_age, PRECISION)}")
    average_age = determine_average_age(names_and_ages)
    print(f"{round(average_age, PRECISION)}")


def determine_median_age(names_and_ages: list) -> float:
    mid_start_index = (len(names_and_ages) - 1) // 2
    mid_stop_index = (len(names_and_ages) // 2) + 1
    sorted_by_age = sorted(names_and_ages, key=itemgetter(1))
    middle_elements = sorted_by_age[mid_start_index:mid_stop_index]
    return determine_average_age(middle_elements)


def determine_average_age(names_and_ages: list) -> float:
    # The following line uses list comprehension. See chapter 7.11
    just_ages = [row[1] for row in names_and_ages]
    average_age = sum(just_ages) / len(just_ages) if len(just_ages) > 0 else 0
    return average_age


if __name__ == "__main__":
    main()
