answer = input("You need something doubled? (Y)es?\n")
while answer == "Y":
    number = float(
        input("All right, then. Give me a number, and I'll double it for ya:\n")
    )
    doubled = 2 * number
    print(f"{doubled:.6f}")

    answer = input("You need something else doubled? (Y)es?\n")

