from importlib import import_module
from pathlib import Path


CLASS_PLAYER = "Player"
CLASS_TEAM = "Team"


def main():
    requested_method = input()
    class_name, method_name = requested_method.split(".")
    if class_name == CLASS_PLAYER:
        test_player(method_name)
    elif class_name == CLASS_TEAM:
        test_team(method_name)
    else:
        assert False, f"Unknown class {class_name} requested."


def test_player(requested_method):
    Player = get_class(CLASS_PLAYER)
    available_methods = {
        "__init__": test_player_init,
        "__str__": test_player_str,
        "add_goals": test_player_add_goals,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run(Player)


def test_team(requested_method):
    Team = get_class(CLASS_TEAM)
    Player = get_class(CLASS_PLAYER)
    available_methods = {
        "__init__": test_team_init,
        "__str__": test_team_str,
        "add_player": test_team_add_player,
        "most_goals_player": test_team_most_goals_player,
        "__add__": test_team_add,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run(Team, Player)


def test_player_init(Player):
    assert hasattr(
        Player, "__init__"
    ), f"Could not find member function '__init__' of class 'Player'"

    parameters = Player.__init__.__code__.co_varnames
    expected_number_of_parameters = 3  # 2 + self
    assert len(parameters) >= expected_number_of_parameters, (
        f"Unexpected number of parametes, {len(parameters)}.",
    )

    # Arrange
    number_of_specified = 2
    player_inputs = [input() for _ in range(number_of_specified)]
    print(f"Initializing Player.")

    for name, value in zip(["First name", "Last name"], player_inputs):
        print(f" {name} = {value}")

    # Act
    try:
        instance = Player(*player_inputs)
    except Exception as e:
        print(f"Error calling constructor: {e}")
        raise

    # Assert
    print(f"Player created without errors.")

    return instance


def test_player_str(Player):
    assert hasattr(
        Player, "__str__"
    ), f"Could not find member function '__str__' of class 'Player'"

    # Arrange
    instance = test_player_init(Player)

    # Act
    try:
        representation = str(instance)
    except Exception as e:
        print(f"Error getting player string representation: {e}")
        raise

    # Assert
    print(representation)

    assert (
        representation is not None
    ), f"'__str__' method returned 'None', but should return a string."
    assert isinstance(
        representation, str
    ), f"'__str__' method returned '{type(representation)}', but should return 'str'."
    first_time = representation
    second_time = str(instance)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the '__str__' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_player_add_goals(Player):
    assert hasattr(
        Player, "add_goals"
    ), f"Could not find member function 'add_goals' of class 'Player'"

    # Arrange
    instance = test_player_init(Player)
    player_before = str(instance)
    print("Player:")
    print(instance)
    goal_amount = int(input())

    # Act
    try:
        result = instance.add_goals(goal_amount)
    except Exception as e:
        print(f"Error getting adding goals to a Player: {e}")
        raise

    # Assert
    print(f"Player after adding goals :")
    print(instance)

    assert result is None, "\n".join(
        [
            f"Method 'add_goals' is not supposed to return anything.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    player_after = str(instance)
    assert player_before != player_after, "\n".join(
        [
            f"The operation appears to not have changed the player.",
            f"Before: '{player_before}'.",
            f"After:  '{player_after}'.",
            "The amount of goals should stay changed.",
        ]
    )


def test_team_init(Team, Player=None):
    assert hasattr(
        Team, "__init__"
    ), f"Could not find member function '__init__' of class 'Team'"

    parameters = Team.__init__.__code__.co_varnames
    expected_number_of_parameters = 2  # 1 + self
    assert len(parameters) >= expected_number_of_parameters, (
        f"Unexpected number of parametes, {len(parameters)}.",
    )

    # Arrange
    team_name = input()
    print(f"Initializing Team.")

    print(f" Name = {team_name}")

    # Act
    try:
        instance = Team(team_name)
    except Exception as e:
        print(f"Error calling constructor: {e}")
        raise

    # Assert
    print(f"Team created without errors.")

    return instance


def test_team_str(Team, Player):
    assert hasattr(
        Team, "__str__"
    ), f"Could not find member function '__str__' of class 'Team'"

    # Arrange
    instance = test_team_init(Team)

    # Act
    try:
        representation = str(instance)
    except Exception as e:
        print(f"Error getting team string representation: {e}")
        raise

    # Assert
    print(representation)

    assert (
        representation is not None
    ), f"'__str__' method returned 'None', but should return a string."
    assert isinstance(
        representation, str
    ), f"'__str__' method returned '{type(representation)}', but should return 'str'."
    first_time = representation
    second_time = str(instance)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the '__str__' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_team_add_player(Team, Player):
    assert hasattr(
        Team, "add_player"
    ), f"Could not find member function 'add_player' of class 'Team'"

    assert hasattr(
        Player, "__init__"
    ), f"Could not find member function '__init__' of class 'Player'"

    # Arrange
    instance = test_team_init(Team)
    player = test_player_init(Player)
    team_before = str(instance)
    print("Team:")
    print(instance)

    # Act
    try:
        result = instance.add_player(player)
    except Exception as e:
        print(f"Error getting adding player to a Team: {e}")
        raise

    # Assert
    print(f"Team after adding player :")
    print(instance)

    assert result is None, "\n".join(
        [
            f"Method 'add_player' is not supposed to return anything.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    team_after = str(instance)
    assert team_before != team_after, "\n".join(
        [
            f"The operation appears to not have changed the player.",
            f"Before: '{team_before}'.",
            f"After:  '{team_after}'.",
            "The amount of goals should stay changed.",
        ]
    )


def test_team_most_goals_player(Team, Player):
    assert hasattr(
        Team, "most_goals_player"
    ), f"Could not find member function 'most_goals_player' of class 'Team'"

    # Arrange
    instance = test_team_init(Team)
    player1 = test_player_init(Player)
    player2 = test_player_init(Player)

    goal_amount1 = int(input())
    goal_amount2 = int(input())

    player1.add_goals(goal_amount1)
    player2.add_goals(goal_amount2)

    instance.add_player(player1)
    instance.add_player(player2)
    print("Team:")
    print(instance)
    team_before = str(instance)

    # Act
    try:
        result = instance.most_goals_player()
    except Exception as e:
        print(f"Error getting finding player with most goals in Team: {e}")
        raise

    print(result)
    # Assert

    assert isinstance(result, Player), "\n".join(
        [
            f"Method 'most_goals_player' did not return a player as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    team_after = str(instance)
    assert team_before == team_after, "\n".join(
        [
            f"The operation appears to have changed the team.",
            f"Before: '{team_before}'.",
            f"After:  '{team_after}'.",
            "The team should stay unchanged.",
        ]
    )


def test_team_add(Team, Player):
    assert hasattr(
        Team, "__add__"
    ), f"Could not find member function '__add__' of class 'Team'"

    # Arrange
    instance1 = test_team_init(Team)
    instance2 = test_team_init(Team)
    player1 = test_player_init(Player)
    player2 = test_player_init(Player)

    instance1.add_player(player1)
    instance2.add_player(player2)

    before_team1 = str(instance1)
    before_team2 = str(instance2)
    print("Team 1:")
    print(instance1)
    print("Team 2:")
    print(instance2)

    # Act
    try:
        result = instance1 + instance2
    except Exception as e:
        print(f"Error adding Teams: {e}")
        raise

    # Assert
    print(f"Result of adding {instance1} and {instance2} together:")
    print(result)

    assert isinstance(result, Team), "\n".join(
        [
            f"Method '__add__' did not return a Team, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_team1 = str(instance1)
    after_team2 = str(instance2)
    assert before_team1 == after_team1, "\n".join(
        [
            f"The addition appears to have changed the first team.",
            f"Before: '{before_team1}'.",
            f"After:  '{before_team1}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_team2 == after_team2, "\n".join(
        [
            f"The addition appears to have changed the second team.",
            f"Before: '{before_team2}'.",
            f"After:  '{after_team2}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = str(result)
    second_time = str(instance1 + instance2)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the addition has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def get_class(name):
    for module in load_modules():
        if hasattr(module, name):
            return getattr(module, name)

    raise NameError(f"Could not find class {name}.")


def load_modules():
    modules = []
    this_file = Path(__file__)
    for submission_file in this_file.parent.iterdir():
        if submission_file == this_file:
            continue

        if submission_file.suffix == ".py":
            modules.append(import_module(submission_file.stem))

    return modules


if __name__ == "__main__":
    main()
