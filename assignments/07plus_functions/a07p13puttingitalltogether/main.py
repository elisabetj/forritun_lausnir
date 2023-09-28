from solution_code import move_many


def main():
    run_with_ui_and_default_setup()
    # run_like_gradescope()


def run_with_ui_and_default_setup():
    # You can use this code to test your solution:
    number_of_discs = int(input("How many discs are on the left-most pillar? "))
    initial_state = ""
    for disc in range(number_of_discs, 0, -1):
        initial_state += str(disc)
    initial_state += "|||"
    print(initial_state)
    move_many(how_many=number_of_discs, from_pillar=1, to_pillar=3, state=initial_state)


def run_like_gradescope():
    # But this is how Gradescope will test it:
    number_of_discs = int(input())
    from_pillar = int(input())
    to_pillar = int(input())
    state = input()
    move_many(number_of_discs, from_pillar, to_pillar, state)


if __name__ == "__main__":
    main()
