# The following constants indicate the position of the respective
# fields in the tuple stored as the value for the key in the players dictionary
RANK = 0
COUNTRY = 1
RATING = 2
BIRTHYEAR = 3


def main():
    filename = input()
    file_stream = open_file(filename)
    if file_stream is None:
        print(f"File {filename} not found!")
        return

    with file_stream:  # This takes care of closing the file for us.
        players_by_name = create_players_dict(file_stream)

    country_lists = group_by(players_by_name, COUNTRY)
    print_header("Players by country:")
    print_sorted(country_lists, players_by_name)

    print()

    year_lists = group_by(players_by_name, BIRTHYEAR)
    print_header("Players by birth year:")
    print_sorted(year_lists, players_by_name)


def open_file(filename):
    """Opens the file with the given file name.

    Returns the corresponding file stream, or None if the file cannot be opened.
    """

    try:
        file_stream = open(filename)
        return file_stream
    except FileNotFoundError:
        return None


def create_players_dict(file_stream) -> dict:
    """Reads the given file stream and returns the contents in a dictionary.

    A key in the dictionary is the name of a chess player,
    and the corresponding value is a tuple: (rank, country, rating, birth-year).
    """

    players_info: dict = {}
    for line in file_stream:
        rank, name, country, rating, birth_year = line.split(";")

        # The name is one field separated by ","
        last_name, first_name = name.split(",")

        # Strip leading spaces
        first_name = first_name.strip()
        last_name = last_name.strip()
        country = country.strip()

        name = f"{first_name} {last_name}"
        players_info[name] = (int(rank), country, int(rating), int(birth_year))

    return players_info


def group_by(players_info: dict, attribute_key: int) -> dict:
    """Uses a players dictionary to create a new dictionary.

    A key in the new dictionary is a given attribute of the player,
    and the corresponding value is a list of player names.
    """

    organized_by_attribute: dict = {}
    for chess_player, chess_player_data in players_info.items():
        attribute = chess_player_data[attribute_key]

        if attribute not in organized_by_attribute:
            organized_by_attribute[attribute] = []

        organized_by_attribute[attribute].append(chess_player)

    return organized_by_attribute


def print_header(header: str) -> None:
    """Prints the header, followed by an equally long line of dashes."""

    print(header)
    dashes = "-" * len(header)
    print(dashes)


def print_sorted(organized_by_attribute: dict, players_info: dict) -> None:
    """Prints information sorted by the chosen attribute."""

    sorted_by_attribute_first_and_then_names = sorted(organized_by_attribute.items())
    for attribute, players in sorted_by_attribute_first_and_then_names:
        average_rating = get_average_rating(players, players_info)
        print(f"{attribute} ({len(players)}) ({average_rating:.1f}):")

        for player_name in players:
            rating = players_info[player_name][RATING]
            print(f"{player_name:>40}{rating:>10}")


def get_average_rating(players: list, players_info: dict) -> float:
    """Returns the average ratings for the given players."""

    ratings = [players_info[player][RATING] for player in players]
    average = sum(ratings) / len(ratings)
    return average


if __name__ == "__main__":
    main()
