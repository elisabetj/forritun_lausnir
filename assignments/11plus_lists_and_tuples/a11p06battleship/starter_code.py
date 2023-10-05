SHIPS_AND_SIZES = (
    ("carrier", 5),
    ("battleship", 4),
    ("destroyer", 3),
    ("submarine", 3),
    ("patrol boat", 2),
)
# Input prompt string:
# f"Location and orientation of your {ship}:\n"

def main():
    # You can use this game loop if you'd like
    fleet = gather_fleet_positions()
    while something_is_still_afloat(fleet):
        coordinates = ask_where_to_attack()
        ship = get_ship_at(coordinates, fleet)
        if ship:
            report_hit(ship, coordinates)
        else:
            report_miss()

    print("The entire fleet has been sunk")


# ... add your functions here


if __name__ == "__main__":
    main()
