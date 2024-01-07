#!/usr/bin/python3

from io import TextIOWrapper
from typing import List, Tuple, Dict, Union


def main():
    entries = get_data()
    if entries is None:
        return

    competitors = collect_attempts(entries)
    display_output(competitors)


def get_data() -> Union[List[Tuple[str, float]], None]:
    file_name = input()
    try:
        with open(file_name) as file:
            return extract_data(file)
    except FileNotFoundError:
        return None


def extract_data(file: TextIOWrapper) -> List[Tuple[str, float]]:
    entries = []
    for line in file:
        first_name, last_name, throw = line.split()
        name = f"{first_name} {last_name}"
        throw = float(throw)
        entries.append((name, throw))

    return entries


def collect_attempts(entries: List[Tuple[str, float]]) -> Dict[str, List[float]]:
    competitors: Dict[str, List] = {}
    for name, throw in entries:
        if name not in competitors:
            competitors[name] = []

        competitors[name].append(throw)

    return competitors


def display_output(competitors: Dict[str, List[float]]) -> None:
    multiple_throws = []
    for name, lengths in competitors.items():
        rounded = [f"{length:.2f}" for length in lengths]
        print(f"{name:<20}Throws: {' '.join(rounded)}")
        if len(lengths) > 1:
            average = sum(lengths) / len(lengths)
            multiple_throws.append((name, average))

    if multiple_throws:
        highest = 0
        best = ""
        for name, average in multiple_throws:
            if average > highest:
                highest = average
                best = name

        print(f"{best}: {highest:.2f}")


if __name__ == "__main__":
    main()
