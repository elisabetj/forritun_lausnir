import sys

COUNTRIES_OF_THE_WORLD = "base_countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "


def main():
    country_suffix = input()
    file_object = open_file(COUNTRIES_OF_THE_WORLD)

    display_countries(file_object, country_suffix)

    file_object.close()


def open_file(file_name):
    return open(file_name, "r")


def display_countries(file_object, suffix):
    count = 0
    for line in file_object:
        country = line.strip()
        if country.endswith(suffix):
            print(country)
            count += 1

    print(f"{count} countries with suffix {suffix} in total.")


if __name__ == "__main__":
    main()
