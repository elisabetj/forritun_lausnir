#!/usr/bin/env python3


def main():
    number_of_bags, bennis_bag = [int(item) for item in input().split()]

    bags = [int(bag) for bag in input().split()]
    assert len(bags) == number_of_bags

    assert bennis_bag in bags
    index_of_bennis_bag = bags.index(bennis_bag)
    assert 0 <= index_of_bennis_bag < number_of_bags

    if index_of_bennis_bag == 0:
        print("fyrst")
    elif index_of_bennis_bag == 1:
        print("naestfyrst")
    else:
        assert 2 <= index_of_bennis_bag < number_of_bags
        print(f"{index_of_bennis_bag + 1} fyrst")


if __name__ == "__main__":
    main()
