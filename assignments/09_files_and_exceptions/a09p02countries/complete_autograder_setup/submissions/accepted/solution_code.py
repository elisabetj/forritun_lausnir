import sys

COUNTRIES_OF_THE_WORLD = "countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "


def main():
    country_suffix = get_suffix()
    file_object = open_file(COUNTRIES_OF_THE_WORLD)

    display_countries(file_object, country_suffix)

    file_object.close()


def get_suffix():
    return input()


def open_file(file_name):
    file_object = open(file_name, "r")
    # Remember that "r" is the default value of the mode parameter,
    # so there is actually no need to specify it.
    # This is equivalent to:

    # file_object = open_file(file_name)

    return file_object


def display_countries(file_object, suffix):
    """Prints all countries ending with the given suffix, appearing in the given file."""
    count = 0
    for line in file_object:
        country = line.strip()
        if country.endswith(suffix):
            print(country)
            count += 1

    print(f"{count} countries with suffix {suffix} in total.")


# You'll often see the following two lines at the bottom of python files.
# This is a good way of setting up the program.
# It checks if this file is being run as the main program.
#
# Python modules have a special attribute called __name__,
# which indicates whether the file is being run as the main program,
# or being imported into another module.
#
# If it is being run, then its __name__ attribute will be "__main__".
# But if it is being imported, it's __name__ will be the name of the .py file.
#
# In case it is being imported, we don't want to run any functions, just import their names.
# But if it is being run, then we call the main() function to start the program.
if __name__ == "__main__":
    main()
