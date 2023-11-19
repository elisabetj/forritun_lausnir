#!/usr/bin/python3
import random
import sys
from string import ascii_letters, digits
from typing import Tuple


INVALID = ascii_letters
MIXED = INVALID + digits

random.seed(sys.argv[-1])


STARTING_POINTS = 301
PLAYER1 = "Player 1"
PLAYER2 = "Player 2"


def main():
    """Runs the main loop of the game."""

    player1_remaining_points = STARTING_POINTS
    player2_remaining_points = STARTING_POINTS

    game_over = False
    while not game_over:
        game_over, player1_remaining_points = round_for_player(
            PLAYER1, player1_remaining_points
        )
        if not game_over:
            game_over, player2_remaining_points = round_for_player(
                PLAYER2, player2_remaining_points
            )


def round_for_player(player, remaining_points: int) -> Tuple[bool, int]:
    """Runs a round for the given player.

    Returns (game_over, remaining_points) after the round.
    """

    points = get_error_free_points(player)
    remaining_points = subtract_points(points, remaining_points)
    game_over = remaining_points == 0

    return game_over, remaining_points


def get_error_free_points(player):
    """Gets the points scored by the given player,
    repeatedly until a valid score is entered.
    """

    while (points := get_points_scored(player)) is None:
        pass

    return points


def get_points_scored(player):
    """Reads the points scored by the given player from the user.

    Returns None if invalid input, otherwise the points scored.
    """

    valid = random.choice([True, False])
    if valid:
        score = random_valid()
        print(score)
        return score
    else:
        print(random_invalid())


def random_valid():
    return sum([random_score() for _ in range(3)])


def random_score():
    slice = random.randint(0, 22)
    if slice == 21:
        return 25
    if slice == 22:
        return 50

    multiplier = random.randint(1, 3)
    score = slice * multiplier
    return score


def random_invalid():
    length = random.randrange(0, 3)
    if length == 0:
        return ""

    not_a_number = [random.choice(INVALID)]
    not_a_number += random.choices(MIXED, k=length - 1)
    random.shuffle(not_a_number)
    return "".join(not_a_number)


def subtract_points(points, remaining_points):
    """Subtracts the points from the remaining points, if applicable.

    Returns the changed or unchanged remaining points.
    """

    if points <= remaining_points:
        remaining_points -= points

    return remaining_points


if __name__ == "__main__":
    main()
