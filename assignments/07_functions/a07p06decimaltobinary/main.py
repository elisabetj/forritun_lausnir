from solution_code import decimal_to_binary


def main():
    # run()
    run_with_ui()


def run():
    number_as_decimal = int(input())
    binary_representation = decimal_to_binary(number_as_decimal)
    print(binary_representation)


def run_with_ui():
    number_as_decimal = int(input("Enter a number to convert: "))
    binary_representation = decimal_to_binary(number_as_decimal)
    print(
        f"The binary representation of {number_as_decimal}",
        f"is {binary_representation}.",
    )


if __name__ == "__main__":
    main()
