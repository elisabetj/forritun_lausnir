from typing import Tuple
import random


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


def main():
    initialize()

    play()
    while play_again():
        play()


def initialize() -> None:
    the_seed = int(input("Input seed:\n"))
    random.seed(the_seed)


def play():
    """Plays the game."""

    total_coins = 0
    moves = 0

    location = STARTING_LOCATION
    while location != FINAL_DESTINATION:
        location, total_coins = play_one_move(location, total_coins)
        moves += 1

    print(f"Victory! Total coins {total_coins}. Moves {moves}.")


def play_one_move(location: Tuple[int], total_coins: int) -> tuple:
    """Plays one move of the game.

    Returns updated location and coins.
    """

    valid_directions = find_directions(location)
    direction = get_direction(valid_directions)

    if direction in valid_directions:
        location = move(direction, location)
        total_coins = update_coins(location, total_coins)
    else:
        print("Not a valid direction!")

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
    print_directions(valid_directions)

    direction = get_random_direction()
    print(f"Direction: {direction}")

    return direction


def print_directions(available_directions: Tuple[str]) -> None:
    print("You can travel: ", end="")

    one_done_already = False
    for direction in available_directions:
        if one_done_already:
            print(" or ", end="")

        if direction == NORTH:
            print("(N)orth", end="")
        elif direction == EAST:
            print("(E)ast", end="")
        elif direction == SOUTH:
            print("(S)outh", end="")
        elif direction == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


def get_random_direction() -> str:
    return random.choice([NORTH, EAST, SOUTH, WEST])


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


def update_coins(location: Tuple[int], total_coins: int) -> int:
    coins = get_coins(location)
    total_coins += coins
    if coins > 0:
        print_coins(coins, total_coins)

    return total_coins


def get_coins(location: Tuple[int]) -> int:
    if location in CELLS_WITH_COINS:
        answer = random.choice([YES, NO])
        print(f"Pull a lever ({YES}/{NO}): {answer}")
        if answer == YES:
            return 1
    return 0


def print_coins(coins: int, total_coins: int) -> None:
    amount = "1 coin" if coins == 1 else f"{coins} coins"
    print(f"You received {amount}, your total is now {total_coins}.")


def play_again() -> bool:
    answer = input("Play again (y/n):\n")
    return answer.lower() == YES


if __name__ == "__main__":
    main()
