#!/usr/bin/python3
def main():
    number_of_chores = int(input())
    seen = set()
    todo = []
    for _ in range(number_of_chores):
        chore = input()

        if chore not in seen:
            todo.append(chore)

        seen.add(chore)

    for chore in todo:
        print(chore)


if __name__ == "__main__":
    main()
