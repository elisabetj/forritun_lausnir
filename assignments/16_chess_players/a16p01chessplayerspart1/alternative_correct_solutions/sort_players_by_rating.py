from typing import List, Tuple, Dict

# The following constants indicate the position of the respective
# fields in the tuple stored as the value for the key in the players dictionary
RANK = 0
COUNTRY = 1
RATING = 2
BIRTHYEAR = 3


def main():
    """Reads a file with info on top 100 chess players and displays in a table."""

    players_by_name = get_data()
    if players_by_name is None:
        return

    players_by_countries = group_by_countries(players_info=players_by_name)
    display_table(country_lists=players_by_countries, players_info=players_by_name)


def get_data() -> Dict[str, Tuple[int, str, int, int]] | None:
    """Gets data about chess players from file supplied by the user."""
    filename = input()
    try:
        with open(filename) as file:
            return record_player_info(file)
    except FileNotFoundError:
        return None


def record_player_info(file) -> Dict[str, Tuple[int, str, int, int]]:
    """Creates a record of player information which enables fast lookup by player name."""
    players = {}
    for line in file:
        name, rank, country, rating, year = parse_line(line)
        players[name] = (rank, country, rating, year)

    return players


def parse_line(line: str) -> Tuple[str, int, str, int, int]:
    """Interprets a single line from the file."""
    rank, name, country, rating, year = line.split(";")
    last_name, first_name = name.split(",")
    full_name = f"{first_name.strip()} {last_name.strip()}"

    return full_name, int(rank), country.strip(), int(rating), int(year)


def group_by_countries(
    players_info: Dict[str, Tuple[int, str, int, int]],
) -> Dict[str, List[str]]:
    """Processes the player information record to enable fast lookup by country.

    Returns a dictionary, where
        a key is a country,
        and the corresponding value is a list of player names.
    """

    country_lists: dict = {}
    for player_name, data_for_player in players_info.items():
        country = data_for_player[COUNTRY]

        if country not in country_lists:
            country_lists[country] = []

        country_lists[country].append(player_name)

    return country_lists


def display_table(
    country_lists: Dict[str, List[str]],
    players_info: Dict[str, Tuple[int, str, int, int]],
) -> None:
    """Prints a table with a header and lists of players from the countries."""
    print_header(f"Players by country:")
    for country, player_list in sorted(country_lists.items()):
        print_country(country, player_list, players_info)


def print_header(header: str) -> None:
    """Prints the header, followed by an equally long line of dashes."""
    dashes = "-" * len(header)
    print(header)
    print(dashes)


def print_country(
    country: str,
    players_from_country: List[str],
    player_info: Dict[str, Tuple[int, str, int, int]],
) -> None:
    """Prints a summary header line, followed by a list of all players from the given country."""
    print_subheader(country, players_from_country, player_info)
    print_players_from_country(players_from_country, player_info)


def print_subheader(
    country: str,
    players: List[str],
    player_info: Dict[str, Tuple[int, str, int, int]],
) -> None:
    """Summarizes the information on the given group of players."""
    number_of_players = len(players)
    average = get_average_rating(players, player_info)
    print(f"{country} ({number_of_players}) ({average:.1f}):")


def get_average_rating(
    players: List[str],
    players_info: Dict[str, Tuple[int, str, int, int]],
) -> float:
    """Returns the average ratings for the given players."""

    ratings = [players_info[name][RATING] for name in players]
    return calculate_average(ratings)


def calculate_average(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0


def print_players_from_country(
    players_from_country: List[str],
    player_info: Dict[str, Tuple[int, str, int, int]],
) -> None:
    ratings = [(player_info[name][RATING], name) for name in players_from_country]
    ratings.sort(reverse=True)
    for rating, name in ratings:
        print(f"{name:>40}{rating:>10}")


if __name__ == "__main__":
    main()
