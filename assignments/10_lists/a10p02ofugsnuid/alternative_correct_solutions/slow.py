#! /usr/bin/env python3


def main():
    number_of_inputs = int(input())

    inputs = []
    for _ in range(number_of_inputs):
        # We can also prepend the inputs each time,
        # so that the list will already be reversed as we build it,
        # but that's a slower operation,
        # as you'll learn about in the course on Data Structures,
        # because when we insert an element at the front,
        # Python needs to move all the other elements backwards by one step,
        # and again when we insert the next element and so on,
        # more and more elements as the list gets longer.
        inputs.insert(0, input())

    for index in range(number_of_inputs):
        print(inputs[index])


if __name__ == "__main__":
    main()
