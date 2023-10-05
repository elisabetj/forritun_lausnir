#!/usr/bin/python3
import random
import sys

from string import ascii_uppercase

random.seed(sys.argv[-1])


SHIPS_AND_SIZES = (
    ("carrier", 5),
    ("battleship", 4),
    ("destroyer", 3),
    ("submarine", 3),
    ("patrol boat", 2),
)

tile_rows = ascii_uppercase[:10]
tile_columns = list(map(str, range(1, 11)))
all_tiles = [f"{r}{c}" for r in tile_rows for c in tile_columns]


def get_valid_placement(size):
    bound_rows = tile_rows[: size + 1]
    bound_columns = tile_columns[: size + 1]
    hori_or_vert = random.choice((0, 1))

    if hori_or_vert:
        row = random.choice(tile_rows)
        column = random.choice(bound_columns)
        coordinates = f"{row}{column}"
        orientation = "horizontal"
        occupied_tiles = [f"{row}{c}" for c in range(int(column), int(column) + size)]
    else:
        row = random.choice(bound_rows)
        column = random.choice(tile_columns)
        coordinates = f"{row}{column}"
        orientation = "vertical"
        start_index = tile_rows.index(row)
        occupied_tiles = [
            f"{r}{column}" for r in tile_rows[start_index : start_index + size]
        ]
    return coordinates, orientation, occupied_tiles


def overlap_check(positions, occupied_tiles):
    if positions == []:
        return False

    for _, ship_tiles, _ in positions:
        for tile in ship_tiles:
            if tile in occupied_tiles:
                return True
    return False


def gather_fleet_positions() -> list:
    positions = []
    for ship, size in SHIPS_AND_SIZES:
        coordinate, orientation, occupied_tiles = get_valid_placement(size)
        while overlap_check(positions, occupied_tiles):
            coordinate, orientation, occupied_tiles = get_valid_placement(size)

        print(f"{coordinate} {orientation}")
        positions.append((ship, occupied_tiles, []))
    return positions


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


random.shuffle(all_tiles)  # attack moves

fleet = gather_fleet_positions()
while something_is_still_afloat(fleet):
    print(all_tiles[-1])
    coordinates = all_tiles.pop()

    ship = get_ship_at(coordinates, fleet)
    if ship:
        _, _, hits = ship
        hits.append(coordinates)
