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
    entries: List[Tuple[str, float]] = []
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
    """Display the list of throws for each competitor, and then the winner."""
    display_competitor_throws(competitors)
    report_winner(competitors)


def display_competitor_throws(competitors: Dict[str, List[float]]) -> None:
    """Print the list of competitors along with their throws."""
    for name, lengths in competitors.items():
        length_strings = [str(length) for length in lengths]
        print(f"{name:<20}Throws: {' '.join(length_strings)}")


def report_winner(competitors: Dict[str, List[float]]) -> None:
    """Report the competitor with the highest average."""
    multiple_throws = filter_on_multiple_attempts(competitors)
    if multiple_throws:
        best, highest = determine_winner(multiple_throws)
        print(f"{best}: {round(highest, 2)}")


def filter_on_multiple_attempts(
    competitors: Dict[str, List[float]],
    minimum_number_of_attempts: int = 2,
) -> Dict[str, List[float]]:
    """Narrow the focus to those competitors with enough throws."""
    return {
        name: throws
        for name, throws in competitors.items()
        if len(throws) >= minimum_number_of_attempts
    }


def determine_winner(
    repeat_throwers: Dict[str, List[float]],
) -> Tuple[str, float]:
    """Find the competitor with the highest average throw.

    Return the name and the average of said competitor.
    In case of ties, return the first found.
    """
    best, highest = "", 0
    for name, throws in repeat_throwers:
        average = calculate_average(throws)
        if average > highest:
            best, highest = name, average

    return best, highest


def calculate_average(lengths: List[float]) -> float:
    """Find the average of the given list of throws."""
    return sum(lengths) / len(lengths) if lengths else 0


if __name__ == "__main__":
    main()
