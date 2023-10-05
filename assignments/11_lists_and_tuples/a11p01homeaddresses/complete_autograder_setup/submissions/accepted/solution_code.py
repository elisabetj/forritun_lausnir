from typing import List, Tuple

NO_MORE = "q"


def main() -> None:
    home_addresses = get_home_addresses()
    print(home_addresses)
    street_and_number = get_tuple_from_home_addresses(home_addresses)
    print(street_and_number)


def get_home_addresses() -> List[str]:
    home_addresses = []

    home_address = input()
    while home_address.lower() != NO_MORE:
        home_addresses.append(home_address)
        home_address = input()

    return home_addresses


def get_tuple_from_home_addresses(home_addresses: List[str]) -> List[Tuple[str]]:
    street_and_number = []
    for address in home_addresses:
        street_and_number.append(tuple(address.split()))

    return street_and_number


if __name__ == "__main__":
    main()
