import re
import sys

from typing import Tuple


# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

YES = "y"
NO = "n"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)
CELLS_WITH_COINS = [(1, 2), (2, 2), (2, 3), (3, 2)]

MAX_MOVES_PER_GAME = 50
MAX_REPETITIONS = 10


def main():
    repetitions = 1
    play()
    while play_again():
        repetitions += 1
        play()

    assert repetitions <= MAX_REPETITIONS
    assert sys.stdin.read() == "", "Trailing input after declining to play again."
    sys.exit(42)


def play():
    move_count = 0
    total_coins = 0

    location = STARTING_LOCATION
    while location != FINAL_DESTINATION:
        location, total_coins = play_one_move(location, total_coins)
        move_count += 1

    assert move_count <= MAX_MOVES_PER_GAME


def play_one_move(location: Tuple[int], total_coins: int) -> tuple:
    """Plays one move of the game.

    Returns updated location and coins.
    """

    valid_directions = find_directions(location)
    direction = get_direction(valid_directions)

    if direction in valid_directions:
        location = move(direction, location)
        total_coins = update_coins(location, total_coins)

    return location, total_coins


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
    line = sys.stdin.readline()
    assert re.match("^[newsNEWS]\n$", line), "Invalid direction."
    return line.strip().lower()


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
    assert 1 <= x <= 3, "Moved out of bounds on x-coordinate."
    assert 1 <= y <= 3, "Moved out of bounds on y-coordinate."
    return x, y


def update_coins(location: Tuple[int], total_coins: int) -> int:
    coins = get_coins(location)
    total_coins += coins
    return total_coins


def get_coins(location: Tuple[int]) -> int:
    if location in CELLS_WITH_COINS:
        line = sys.stdin.readline()
        assert re.match("^[ynYN]\n$", line), "Invalid response for lever."
        answer = line.strip()
        if answer.lower() == YES:
            return 1

    return 0


def play_again() -> bool:
    line = sys.stdin.readline()
    assert re.match("^[ynYN]\n$", line), "Invalid response for play again."
    answer = line.strip()
    return answer.lower() == YES


if __name__ == "__main__":
    main()
