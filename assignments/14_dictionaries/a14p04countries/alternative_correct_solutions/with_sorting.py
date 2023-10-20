UI = False


def main():
    with get_valid_file() as file:
        country_length_dict = prepare_country_length_dict_from_file(file)

    query_lengths(country_length_dict)
    while more():
        query_lengths(country_length_dict)


def get_valid_file():
    prompt = "Enter a filename:\n" if UI else ""
    file_name = input(prompt)

    while (file_obj := open_file(file_name)) is None:
        print(f"File {file_name} not found!")
        file_name = input(prompt)

    return file_obj


def open_file(file_name):
    try:
        return open(file_name, "r")
    except FileNotFoundError:
        return None


def prepare_country_length_dict_from_file(file_obj):
    country_length_dict = {}

    for line in file_obj:
        country = line.strip()

        if len(country) not in country_length_dict:
            country_length_dict[len(country)] = []

        country_length_dict[len(country)].append(country)

    return country_length_dict


def query_lengths(country_length_dict: dict) -> None:
    prompt = "Enter the length you want to search for:\n" if UI else ""
    user_len = int(input(prompt))
    try:
        print(", ".join(sorted(country_length_dict[user_len])))
    except KeyError:
        print(f"No country name of length {user_len} exists.")


def more() -> bool:
    """Checks if the user wants to examine more countries."""

    prompt = "Would you like to continue (y/n)?:\n" if UI else ""
    answer = input(prompt)
    return answer.lower() != "n"


if __name__ == "__main__":
    main()
