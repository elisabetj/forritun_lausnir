import sys

COUNTRIES_OF_THE_WORLD = "countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "


def main():
    country_suffix = get_suffix()
    with open(COUNTRIES_OF_THE_WORLD) as file_object:
        display_countries(file_object, country_suffix)


def get_suffix():
    sys.stderr.write(INPUT_PROMPT)
    return input()


def display_countries(file_object, suffix):
    """Prints all countries ending with the given suffix, appearing in the given file."""
    count = 0
    for line in file_object:
        country = line.strip()
        if country.endswith(suffix):
            print(country)
            count += 1

    print(f"{count} countries with suffix {suffix} in total.")


if __name__ == "__main__":
    main()
