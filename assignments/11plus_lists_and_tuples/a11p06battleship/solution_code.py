# Possible improvements
# - Validate input can be parsed (coordinates, orientations)
# - Validate that input satisfies game constraints (coordinates within grid, no ships overlap, ships within grid)
# - Make this a humans vs computer game

SHIPS_AND_SIZES = (
    ("carrier", 5),
    ("battleship", 4),
    ("destroyer", 3),
    ("submarine", 3),
    ("patrol boat", 2),
)


def main() -> None:
    fleet = gather_fleet_positions()
    while something_is_still_afloat(fleet):
        coordinates = ask_where_to_attack()
        ship = get_ship_at(coordinates, fleet)
        if ship:
            report_hit(ship, coordinates)
        else:
            report_miss()

    print("The entire fleet has been sunk.")


def gather_fleet_positions() -> list:
    positions = []
    for ship, size in SHIPS_AND_SIZES:
        location = input(f"Location and orientation of your {ship}:\n")
        coordinates, orientation = location.split()
        occupied_tiles = get_occupied_tiles(coordinates, orientation, size)
        positions.append((ship, occupied_tiles, []))
    return positions


def get_occupied_tiles(coordinates: str, orientation: str, size: int) -> list:
    row = coordinates[0].upper()
    column = int(coordinates[1:])
    if orientation.lower() == "horizontal":
        return [f"{row}{c}" for c in range(column, column + size)]
    elif orientation.lower() == "vertical":
        start_index = ord(row)
        return [f"{chr(r)}{column}" for r in range(start_index, start_index + size)]
    else:
        raise ValueError(orientation + " is not a recognized orientation.")


def something_is_still_afloat(fleet: list) -> bool:
    for ship in fleet:
        if is_afloat(ship):
            return True
    return False


def is_afloat(ship: tuple) -> bool:
    _, occupied_tiles, hits = ship
    for tile in occupied_tiles:
        if tile not in hits:
            return True
    return False


def ask_where_to_attack() -> str:
    coordinates = input()
    return coordinates.strip().upper()


def get_ship_at(coordinates: str, fleet: list):
    for ship in fleet:
        if hit_test(ship, coordinates):
            return ship
    return None


def hit_test(ship: tuple, coordinates: str) -> bool:
    _, occupied_tiles, _ = ship
    for tile in occupied_tiles:
        if coordinates == tile:
            return True
    return False


def report_hit(ship: tuple, coordinates: str) -> None:
    name, _, hits = ship
    hits.append(coordinates)
    if is_afloat(ship):
        print(f"Hit, {name}.")
    else:
        print(f"You have sunk my {name}.")


def report_miss() -> None:
    print("Miss.")


if __name__ == "__main__":
    main()
