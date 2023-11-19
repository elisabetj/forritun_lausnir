from typing import Tuple

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
    print(f"{player} remaining points: {remaining_points}")
    if game_over:
        print(f"{player} won!")

    return (game_over, remaining_points)


def get_error_free_points(player):
    """Gets valid points scored by the given player.

    Asks for input repeatedly until a valid score is entered.
    """

    while (points := get_points_scored(player)) is None:
        print("Invalid input!")

    return points


def get_points_scored(player):
    """Reads the points scored by the given player from the user.

    Returns None if invalid input, otherwise the points scored.
    """

    try:
        points = int(input(f"Input points for {player}:\n"))
    except ValueError:
        return None

    return points


def subtract_points(points, remaining_points):
    """Subtracts the points from the remaining points, if applicable.

    Returns the changed or unchanged remaining points.
    """

    if remaining_points >= points:
        remaining_points -= points

    return remaining_points


if __name__ == "__main__":
    main()
