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
    oldest_person = find_oldest_person(names_and_ages)
    name, age = oldest_person
    print(f"The oldest person is {name} who is {age} years old")

    youngest_person = find_youngest_person(names_and_ages)
    name, age = youngest_person
    print(f"The youngest person is {name} who is {age} years old")


def find_oldest_person(names_and_ages: list):
    oldest_person = names_and_ages[0]
    name, max_age = oldest_person

    for person in names_and_ages:
        name, age = person
        if age > max_age:
            max_age = age
            oldest_person = person

    return oldest_person


def find_youngest_person(names_and_ages: list):
    youngest_person = names_and_ages[0]
    _, min_age = youngest_person

    for person in names_and_ages:
        _, age = person
        if age < min_age:
            min_age = age
            youngest_person = person

    return youngest_person


def show_central_tendency_measures(names_and_ages: list):
    # The following line uses list comprehension. See chapter 7.11
    just_ages = [age for name, age in names_and_ages]

    median_age = determine_median_age(just_ages)
    print(f"The median age is {round(median_age, PRECISION)}")

    average_age = determine_average_age(just_ages)
    print(f"The average age is {round(average_age, PRECISION)}")


def determine_median_age(ages: list) -> float:
    sorted_by_age = sorted(ages)
    number_of_people = len(ages)

    if number_of_people % 2 == 1:
        midpoint = number_of_people // 2
        # Here we could just return sorted_by_age[midpoint]
        # but we can also combine flows with the else branch:
        middle_elements = sorted_by_age[midpoint : midpoint + 1]
        # which is what the given solution does.
        # That actually leads to a slightly different result,
        # as the result gets converted to float along the way.
        # So in order to account for that,
        # if we want to return here immediately,
        # we would need to convert to float as well:
        # return float(sorted_by_age[midpoint])
    else:
        right_midpoint = number_of_people // 2
        left_midpoint = right_midpoint - 1
        middle_elements = sorted_by_age[left_midpoint : right_midpoint + 1]

    return determine_average_age(middle_elements)


def determine_average_age(ages: list) -> float:
    average_age = sum(ages) / len(ages) if len(ages) > 0 else 0
    return average_age


if __name__ == "__main__":
    main()
