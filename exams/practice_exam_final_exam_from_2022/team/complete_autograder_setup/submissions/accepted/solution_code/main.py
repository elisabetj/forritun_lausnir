from player import Player
from team import Team


def main():
    requested_method = input()
    available_methods = {
        "Player.__init__": create_player,
        "Player.__str__": print_player,
        "Player.add_goals": add_player_goals,
        "Team.__init__": create_team,
        "Team.__str__": print_team,
        "Team.add_player": add_player_team,
        "Team.most_goals_player": most_goals_player_team,
        "Team.__add__": add_team,
    }

    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run()


def create_player():
    number_of_specified = 2
    player_inputs = [input() for _ in range(number_of_specified)]
    print(f"Initializing Player.")

    for name, value in zip(["First name", "Last name"], player_inputs):
        print(f" {name} = {value}")

    instance = Player(*player_inputs)

    print(f"Player created without errors.")

    return instance


def print_player(player=None):
    if player is None:
        player = create_player()

    print(player)


def add_player_goals(player=None):
    if player is None:
        player = create_player()

    print("Player:")
    print(player)
    goal_amount = int(input())
    player.add_goals(goal_amount)

    print(f"Player after adding goals :")
    print(player)


def create_team():
    team_name = input()
    print(f"Initializing Team.")

    print(f" Name = {team_name}")

    instance = Team(team_name)

    print(f"Team created without errors.")

    return instance


def print_team(team=None):
    if team is None:
        team = create_team()

    print(team)


def add_player_team(team=None):
    if team is None:
        team = create_team()

    player = create_player()
    print("Team:")
    print(team)

    team.add_player(player)

    print(f"Team after adding player :")
    print(team)


def most_goals_player_team(team=None):
    if team is None:
        team = create_team()

    player1 = create_player()
    player2 = create_player()

    goal_amount1 = int(input())
    goal_amount2 = int(input())

    player1.add_goals(goal_amount1)
    player2.add_goals(goal_amount2)

    team.add_player(player1)
    team.add_player(player2)
    print("Team:")
    print(team)

    result = team.most_goals_player()

    print(result)


def add_team(team1=None, team2=None):
    if team1 is None:
        team1 = create_team()
    if team2 is None:
        team2 = create_team()

    player1 = create_player()
    player2 = create_player()

    team1.add_player(player1)
    team2.add_player(player2)

    print("Team 1:")
    print(team1)
    print("Team 2:")
    print(team2)

    result = team1 + team2

    print(f"Result of adding {team1} and {team2} together:")
    print(result)


if __name__ == "__main__":
    main()
