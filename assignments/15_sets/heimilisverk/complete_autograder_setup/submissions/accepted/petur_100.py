#!/usr/bin/python3
def main():
    number_of_chores = int(input())
    seen = set()
    for _ in range(number_of_chores):
        chore = input()

        if chore not in seen:
            print(chore)

        seen.add(chore)


if __name__ == "__main__":
    main()
