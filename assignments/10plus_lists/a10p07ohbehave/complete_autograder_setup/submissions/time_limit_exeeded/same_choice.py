WOLF = "w"
GOAT = "g"
CABBAGE = "c"
NOTHING = "n"
RIVER = "~"


def main():
    left_side = [WOLF, GOAT, CABBAGE]
    right_side = []
    man_on_left_side = True
    display_state(left_side, right_side, man_on_left_side)

    cargo = get_user_choice(left_side, right_side, man_on_left_side)
    while everything_is_under_control(
        left_side, right_side, man_on_left_side
    ) and not all_have_crossed(right_side):

        man_on_left_side = cross_river(left_side, right_side, man_on_left_side, cargo)
        display_state(left_side, right_side, man_on_left_side)

    announce_fate(left_side, right_side, man_on_left_side)


def display_state(left_side: list, right_side: list, on_left_side: bool):
    print("You are on the left side." if on_left_side else "You are on the right side.")
    print(f"{' '.join(left_side)} {RIVER} {' '.join(right_side)}")


def everything_is_under_control(left_side: list, right_side: list, man_is_on_left_side: bool) -> bool:
    unsupervised_side = right_side if man_is_on_left_side else left_side
    if WOLF in unsupervised_side and GOAT in unsupervised_side:
        return False
    if GOAT in unsupervised_side and CABBAGE in unsupervised_side:
        return False
    return True

def all_have_crossed(destination: list) -> bool:
    return len(destination) == len([WOLF, GOAT, CABBAGE])


def cross_river(left_side: list, right_side: list, man_is_on_left_side: bool, cargo: str) -> bool:
    if cargo != NOTHING:
        transport_cargo(left_side, right_side, man_is_on_left_side, cargo)

    man_is_on_left_side = not man_is_on_left_side
    return man_is_on_left_side


def get_user_choice(left_side: list, right_side: list, man_is_on_left_side: bool) -> str:
    PROMPT = f"What would you like to take over the river? ({WOLF}/{GOAT}/{CABBAGE}/{NOTHING}):\n"
    choice = input(PROMPT).lower()

    while not valid_user_choice(left_side, right_side, man_is_on_left_side, choice):
        print("Not a valid choice!")
        choice = input(PROMPT).lower()

    return choice


def valid_user_choice(left_side: list, right_side: list, man_is_on_left_side: bool, cargo: str) -> bool:
    return (
        cargo == NOTHING
        or cargo in left_side
        and man_is_on_left_side
        or cargo in right_side
        and not man_is_on_left_side
    )


def transport_cargo(left_side: list, right_side: list, from_left_to_right: bool, cargo: str):
    if from_left_to_right:
        left_side.remove(cargo)
        right_side.append(cargo)
    else:
        right_side.remove(cargo)
        left_side.append(cargo)


def announce_fate(left_side: list, right_side: list, man_is_on_left_side: bool):
    if all_have_crossed(right_side):
        print("You solved the puzzle!")
    else:
        print_losing_message(left_side, right_side, man_is_on_left_side)


def print_losing_message(left_side: list, right_side: list, man_is_on_left_side: bool):
    unsupervised_side = right_side if man_is_on_left_side else left_side
    if WOLF in unsupervised_side and GOAT in unsupervised_side:
        print("The wolf ate the goat.")
    elif GOAT in unsupervised_side and CABBAGE in unsupervised_side:
        print("The goat ate the cabbage.")


if __name__ == "__main__":
    main()
