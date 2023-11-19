# The following two constants indicate the position of the respective
# fields in the list stored as the value for the key in the movies dictionary.
RATING = 0
YEAR = 1
# Other constants
PROMPT = "Enter your selection:\n"
MENU_SEPARATOR_LENGTH = 31
MENU_OPTIONS = ["1", "2", "3"]
COL_SEPARATOR = ";"


def main():
    """Reads the input data and starts the main loop."""

    filename = input("Enter filename:\n")
    file_stream = open_file(filename)
    if file_stream is None:
        # missing print statement here
        return

    movies_dict = create_movies_dict(file_stream)
    file_stream.close()
    execute_menu_options(movies_dict)


def open_file(filename):
    """Opens the file with the given file name.

    Returns the corresponding file stream, or None if the file cannot be opened.
    """

    try:
        file_stream = open(filename)
        return file_stream
    except FileNotFoundError:
        return None


def create_movies_dict(file_stream):
    """Reads the given file stream and returns the contents in a dictionary.

    A key in the dictionary is the title of a movie,
    and the corresponding value is a list: [rating, year].
    """

    movies_dict = {}
    for line in file_stream:  # process each line
        title, rating, year = line.split(COL_SEPARATOR)
        movies_dict[title] = [float(rating), int(year)]

    return movies_dict


def execute_menu_options(movies_dict):
    """Executes the menu options selected by the user."""

    selection = ""
    display_menu()
    selection = input(PROMPT)

    while selection in MENU_OPTIONS:
        if selection == MENU_OPTIONS[0]:
            display_movies_alphabetical_order(movies_dict)
        elif selection == MENU_OPTIONS[1]:
            year = int(input("Enter year:\n"))
            display_titles_for_year(movies_dict, year)
        elif selection == MENU_OPTIONS[2]:
            modifier = float(input("Enter modifier for ratings:\n"))
            add_to_ratings(movies_dict, modifier)

        display_menu()
        selection = input(PROMPT)


def display_menu():
    """Displays the menu."""

    print()
    print("*" * MENU_SEPARATOR_LENGTH)
    print(f"{MENU_OPTIONS[0]}. Movies in alphabetical order")
    print(f"{MENU_OPTIONS[1]}. Titles in given year")
    print(f"{MENU_OPTIONS[2]}. Modify all ratings")
    print("*" * MENU_SEPARATOR_LENGTH)
    print()


def display_movies_alphabetical_order(movies_dict):
    """Displays info on the movie in alphabetical order on the titles."""

    for title, info in sorted(movies_dict.items()):
        print(f"{title:<50}{info[RATING]:>6.2f}{info[YEAR]:>6}")


def display_titles_for_year(movies_dict, given_year):
    """Displays the movie titles for the given year."""

    for title, info in movies_dict.items():
        if info[YEAR] == given_year:
            print(title)


def add_to_ratings(movies_dict, modifier):
    """Adds the given modifier to the rating of each movies."""

    for title in movies_dict.keys():
        info = movies_dict[title]
        info[RATING] += modifier


if __name__ == "__main__":
    main()
