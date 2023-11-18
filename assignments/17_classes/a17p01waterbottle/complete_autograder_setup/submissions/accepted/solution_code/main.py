#!/usr/bin/python3

from waterbottle import WaterBottle


def main() -> None:
    requested_method = input()
    available_methods = {
        "__init__": create_bottle,
        "__str__": print_bottle,
        "fill": fill_bottle,
        "drink": take_a_drink,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run()


def create_bottle():
    specification = input()
    assert specification in ["True", "False"]
    no_capacity_specified = eval(specification)
    assert no_capacity_specified in [True, False]

    if no_capacity_specified:
        bottle = WaterBottle()
    else:
        capacity = float(input())
        bottle = WaterBottle(max_capacity=capacity)

    print(
        f"Bottle created.",
        f" Capacity: {bottle.max_capacity:.2f}L.",
        f" Contents: {bottle.current_contents:.2f}L.",
        sep="\n",
    )

    return bottle


def print_bottle(bottle=None):
    if bottle is None:
        bottle = create_bottle()

    print(bottle)


def fill_bottle(bottle=None):
    if bottle is None:
        bottle = create_bottle()

    bottle.fill()

    print(
        f"Bottle filled.",
        f" Contents: {bottle.current_contents:.2f}L.",
        f" Capacity: {bottle.max_capacity:.2f}L.",
        sep="\n",
    )
    print(bottle)


def take_a_drink(bottle=None):
    if bottle is None:
        bottle = create_bottle()
        fill_bottle(bottle)

    appetite = float(input())
    sip = bottle.drink(amount=appetite)
    print(
        f"Bottle sipped.",
        f" Received: {sip:.2f}L.",
        f" Contents: {bottle.current_contents:.2f}L.",
        f" Capacity: {bottle.max_capacity:.2f}L.",
        sep="\n",
    )
    print(bottle)


if __name__ == "__main__":
    main()
