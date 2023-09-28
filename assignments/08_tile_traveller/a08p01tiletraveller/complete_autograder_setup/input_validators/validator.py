import sys

from typing import Tuple


# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)


def main():
    moves_remaining = 200
    location = STARTING_LOCATION
    while location != FINAL_DESTINATION:
        location = play_one_move(location)
        moves_remaining -= 1
        assert moves_remaining > 0, "Too many moves!"
    
    assert not sys.stdin.read()


def play_one_move(location: Tuple[int]) -> Tuple[int]:
    """Plays one move of the game.

    Returns updated location.
    """

    valid_directions = find_directions(location)
    direction = get_direction(valid_directions)
    
    assert direction in [NORTH, EAST, SOUTH, WEST]

    if direction in valid_directions:
        location = move(direction, location)

    return location


def find_directions(location: Tuple[int]) -> Tuple[str]:
    """Returns valid directions as a string given the supplied location."""

    if location == (1, 1):
        valid_directions = (NORTH,)
    elif location == (1, 2):
        valid_directions = NORTH, EAST, SOUTH
    elif location == (1, 3):
        valid_directions = EAST, SOUTH
    elif location == (2, 1):
        valid_directions = (NORTH,)
    elif location == (2, 2):
        valid_directions = SOUTH, WEST
    elif location == (2, 3):
        valid_directions = EAST, WEST
    elif location == (3, 2):
        valid_directions = NORTH, SOUTH
    elif location == (3, 3):
        valid_directions = SOUTH, WEST

    return valid_directions


def get_direction(valid_directions: Tuple[str]) -> str:
    return input().lower()

def move(direction: str, location: Tuple[int]) -> Tuple[int]:
    """Returns updated location given the direction."""

    x, y = location

    if direction == NORTH:
        y += 1
    elif direction == SOUTH:
        y -= 1
    elif direction == EAST:
        x += 1
    elif direction == WEST:
        x -= 1

    return x, y


if __name__ == "__main__":
    main()
    sys.exit(42)
