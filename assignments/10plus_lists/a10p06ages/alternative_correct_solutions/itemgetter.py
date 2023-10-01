from operator import itemgetter

PRECISION = 2


def main():
    names_and_ages = gather_all_inputs()
    show_oldest_and_youngest_persons(names_and_ages)
    show_central_tendency_measures(names_and_ages)


def gather_all_inputs() -> list:
    number_of_people = ask_for_integer()
    names_and_ages = gather_names_and_ages(number_of_people)
    return names_and_ages


def ask_for_integer() -> int:
    reply: str = input()
    while not is_integer(reply):
        print(f"{reply} is not an integer. Please try again.")
        reply = input()

    return int(reply)


def is_integer(string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False


def gather_names_and_ages(how_many: int) -> list:
    names_and_ages: list = []
    for _ in range(how_many):
        name: str = input()
        age: int = ask_for_integer()
        names_and_ages.append([name, age])

    return names_and_ages


def show_oldest_and_youngest_persons(names_and_ages: list):
    oldest_person, max_age = max(names_and_ages, key=itemgetter(1))
    print(f"The oldest person is {oldest_person} who is {max_age} years old")

    youngest_person, min_age = min(names_and_ages, key=itemgetter(1))
    print(f"The youngest person is {youngest_person} who is {min_age} years old")


def show_central_tendency_measures(names_and_ages: list):
    # The following line uses list comprehension. See chapter 7.11
    just_ages = [person[1] for person in names_and_ages]

    median_age = determine_median_age(just_ages)
    print(f"The median age is {round(median_age, PRECISION)}")

    average_age = determine_average_age(just_ages)
    print(f"The average age is {round(average_age, PRECISION)}")


def determine_median_age(ages: list) -> float:
    sorted_by_age = sorted(ages)

    mid_start_index = (len(ages) - 1) // 2
    mid_stop_index = (len(ages) // 2) + 1
    middle_elements = sorted_by_age[mid_start_index:mid_stop_index]

    return determine_average_age(middle_elements)


def determine_average_age(ages: list) -> float:
    average_age = sum(ages) / len(ages) if len(ages) > 0 else 0
    return average_age


if __name__ == "__main__":
    main()
