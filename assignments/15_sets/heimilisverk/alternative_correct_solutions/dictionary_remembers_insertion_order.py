#!/usr/bin/python3
SEEN = None


def main():
    number_of_chores = int(input())
    seen = {}
    for _ in range(number_of_chores):
        chore = input()
        seen[chore] = SEEN

    for chore in seen:
        print(chore)


if __name__ == "__main__":
    main()
