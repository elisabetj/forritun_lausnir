#! /usr/bin/env python3


def main():
    number_of_inputs = int(input())

    inputs = [input() for _ in range(number_of_inputs)]

    for index in range(number_of_inputs, 0, -1):
        print(inputs[index - 1])


if __name__ == "__main__":
    main()
