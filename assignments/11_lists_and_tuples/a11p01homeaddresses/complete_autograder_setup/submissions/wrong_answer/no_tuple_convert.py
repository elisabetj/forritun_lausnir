NO_MORE = "q"


def main():
    home_addresses = get_home_addresses()
    print(home_addresses)
    street_and_number = get_tuple_from_home_addresses(home_addresses)
    print(street_and_number)


def get_home_addresses():
    home_addresses = []

    home_address = input()
    while home_address.lower() != NO_MORE:
        home_addresses.append(home_address)
        home_address = input()

    return home_addresses


def get_tuple_from_home_addresses(home_addresses):
    street_and_number = []
    for address in home_addresses:
        split_address = address.split()
        street_and_number.append(split_address)
    return street_and_number


if __name__ == "__main__":
    main()
