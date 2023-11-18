# The following constants indicate the position of the respective
# fields in the tuple stored as the value for the key in the players dictionary
RANK = 0
COUNTRY = 1
RATING = 2
BIRTHYEAR = 3


def main():
    filename = input("Enter filename: ")
    file_stream = open_file(filename)
    if file_stream is None:
        print(f"File {filename} not found!")
        return

    players_by_name = create_players_dict(file_stream)
    file_stream.close()  # Remember to close the file.

    country_lists = group_by_countries(players_by_name)
    print_header("Players by country:")
    print_sorted(country_lists, players_by_name)


def open_file(filename: str):
    """Opens the file with the given file name.

    Returns the corresponding file stream, or None if the file cannot be opened.
    """

    try:
        file_stream = open("./" + filename)
        return file_stream
    except FileNotFoundError:
        return None


def create_players_dict(file_stream) -> dict:
    """Reads the given file stream and returns the contents in a dictionary.

    A key in the dictionary is the name of a chess player,
    and the corresponding value is a tuple: (rank, country, rating, birth-year).
    """

    players_info: dict = {}
    for line in file_stream:  # process each line
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


def group_by_countries(players_info: dict) -> dict:
    """Uses a players dictionary to create a countries dictionary.

    A key in the dictionary is a country,
    and the corresponding value is a list of player names.
    """

    country_lists: dict = {}
    for chess_player, chess_player_data in players_info.items():
        country = chess_player_data[COUNTRY]

        if country not in country_lists:
            country_lists[country] = []

        country_lists[country].append(chess_player)

    return country_lists


def print_header(header: str) -> None:
    """Prints the header, followed by an equally long line of dashes."""

    print(header)
    dashes = "-" * len(header)
    print(dashes)


def print_sorted(country_lists: dict, players_info: dict) -> None:
    """Prints information sorted by countries."""

    sorted_by_countries_first_and_then_names = sorted(country_lists.items())
    for country, players in sorted_by_countries_first_and_then_names:
        average_rating = get_average_rating(players, players_info)
        print(f"{country} ({len(players)}) ({average_rating:.1f}):")

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
