#!/usr/bin/python3
def main():
    number_of_chores = int(input())
    todo = []
    for _ in range(number_of_chores):
        chore = input()

        if chore not in todo:
            todo.append(chore)

    for chore in todo:
        print(chore)


if __name__ == "__main__":
    main()
