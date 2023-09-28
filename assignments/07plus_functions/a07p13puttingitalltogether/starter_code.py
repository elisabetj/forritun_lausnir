# ... add your functions from the previous solution here at the top


def move_many(
    number_of_discs: int, from_pillar: int, to_pillar: int, state: str
) -> str:
    """Moves the specified number of discs from one pillar to another and returns the updated state representation.

    Prints the state for every move made.
    """

    # ... implement this method


if __name__ == "__main__":
    # You can use this code to test your solution (see also the given main file):
    number_of_discs = int(input("How many discs are on the left-most pillar? "))
    initial_state = ""
    for disc in range(number_of_discs, 0, -1):
        initial_state += str(disc)
    initial_state += "|||"
    print(initial_state)
    move_many(how_many=number_of_discs, from_pillar=1, to_pillar=3, state=initial_state)
