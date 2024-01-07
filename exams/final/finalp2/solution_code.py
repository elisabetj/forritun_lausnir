#!/usr/bin/python3

from typing import List, Tuple, Dict, Union, TextIO


def main():
    entries = get_data()
    if entries is None:
        return

    competitors = collect_attempts(entries)
    display_output(competitors)


def get_data() -> Union[List[Tuple[str, float]], None]:
    """Gets the attempt list from a file supplied by the user."""
    file_name = input()
    try:
        with open(file_name) as file:
            return extract_data(file)
    except FileNotFoundError:
        return None


def extract_data(file: TextIO) -> List[Tuple[str, float]]:
    """Extract a list of throws and the competitor they belong to."""
    entries = []
    for line in file:
        first_name, last_name, throw = line.split()
        name = f"{first_name} {last_name}"
        throw = float(throw)
        entries.append((name, throw))

    return entries


def collect_attempts(
    entries: List[Tuple[str, float]],
) -> Dict[str, List[float]]:
    """Gather the throws into a list for each competitor."""
    competitors: Dict[str, List[float]] = {}
    for name, throw in entries:
        if name not in competitors:
            competitors[name] = []

        competitors[name].append(throw)

    return competitors


def display_output(competitors: Dict[str, List[float]]) -> None:
    """Print the list of competitors along with their throws.

    Conclude by reporting the competitor with the highest average.
    """

    multiple_throws = []
    for name, lengths in competitors.items():
        length_strings = [str(length) for length in lengths]
        print(f"{name:<20}Throws: {' '.join(length_strings)}")

        if len(lengths) > 1:
            average = sum(lengths) / len(lengths)
            multiple_throws.append((name, average))

    if multiple_throws:
        best, highest = determine_winner(multiple_throws)
        print(f"{best}: {round(highest, 2)}")


def determine_winner(
    repeat_throwers: List[Tuple[str, float]],
) -> Tuple[str, float]:
    """Find the competitor with the highest average throw.

    Return the name and the average of said competitor.
    In case of ties, return the first found.
    """
    best, highest = "", 0
    for name, average in repeat_throwers:
        if average > highest:
            best, highest = name, average

    return best, highest


if __name__ == "__main__":
    main()
