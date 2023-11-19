from typing import Dict

STARTING_POINTS = 301
PLAYER1 = "Player 1"
PLAYER2 = "Player 2"


def main():
    """Runs the main loop of the game."""

    scores = {PLAYER1: STARTING_POINTS, PLAYER2: STARTING_POINTS}

    current_player = PLAYER2
    while not game_over(last_player_to_play=current_player, scores=scores):
        current_player = switch_players(previous_player=current_player)
        play_one_turn(current_player, scores)

    print(f"{current_player} won!")


def game_over(last_player_to_play, scores: Dict[str, int]) -> bool:
    """Checks if game is finished."""
    # The game is finished when either player has reached 0 points.
    # But since this is being checked after every turn,
    # it really suffices to check if the last player to play has won.
    return scores[last_player_to_play] == 0


def switch_players(previous_player: str) -> str:
    """Returns the opponent of the previous player."""
    next_player = PLAYER1 if previous_player == PLAYER2 else PLAYER2
    return next_player


def play_one_turn(player, scores: Dict[str, int]) -> None:
    """Runs a round for the given player.

    Updates the score afterwards, and declares the updated points.
    """

    points = get_error_free_points(player)
    subtract_points(points, scores, player)
    print(f"{player} remaining points: {scores[player]}")


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


def subtract_points(points, scores, player):
    """Subtracts the points from the remaining points, if applicable.

    Updates the score for the player, in that case.
    """

    if points <= scores[player]:
        scores[player] -= points


if __name__ == "__main__":
    main()
