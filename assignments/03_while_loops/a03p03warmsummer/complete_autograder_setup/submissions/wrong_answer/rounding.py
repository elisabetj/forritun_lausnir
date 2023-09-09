answer = input("You need something doubled? (Y)es? ")
while answer == "Y":
    number = float(
        input("All right, then. Give me a number, and I'll double it for ya: ")
    )
    doubled = 2 * number
    print(f"{doubled:.2f}")

    answer = input("You need something else doubled? (Y)es? ")

