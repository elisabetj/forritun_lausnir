#!/usr/bin/env python3


def main():
    number_of_bags, bennis_bag = input().split()
    number_of_bags, bennis_bag = int(number_of_bags), int(bennis_bag)

    bags = []
    for bag in input().split():
        bags.append(int(bag))
    assert len(bags) == number_of_bags

    assert bennis_bag in bags
    if bags[0] == bennis_bag:
        print("fyrst")
    elif bags[1] == bennis_bag:
        print("naestfyrst")
    else:
        index = 2
        found = False
        while index < number_of_bags and not found:
            if bags[index] == bennis_bag:
                found = True

            index += 1

        print(f"{index} fyrst")


if __name__ == "__main__":
    main()
