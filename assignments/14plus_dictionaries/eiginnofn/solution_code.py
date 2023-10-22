#!/bin/python3
from typing import Dict

NO_SECOND_NAME = ""


def main():
    residents_present = note_who_is_home()
    handle_queries(residents_present)


def note_who_is_home() -> Dict[str, str]:
    num_currently_present = int(input())
    residents = {}
    for _ in range(num_currently_present):
        name = input()
        record_person(name, residents)

    return residents


def record_person(name: str, residents: Dict[str, str]) -> None:
    names = name.split()
    assert 1 <= len(names) <= 2
    if len(names) == 1:
        (first_name,) = names
        residents[first_name] = NO_SECOND_NAME
    else:
        assert len(names) == 2
        first_name, second_name = names
        residents[first_name] = second_name


def handle_queries(present: Dict[str, str]) -> None:
    number_of_queries = int(input())
    for _ in range(number_of_queries):
        handle_query(present)


def handle_query(present: Dict[str, str]) -> None:
    first_name = input()
    if first_name in present:
        second_name = present[first_name]
        if second_name == NO_SECOND_NAME:
            print("Jebb")
        else:
            print(f"Neibb en {first_name} {second_name} er heima")
    else:
        print("Neibb")


if __name__ == "__main__":
    main()
