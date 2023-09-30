def main():
    num1_str = input()
    num2_str = input()

    result = divide_safe(num1_str, num2_str)

    if result is None:
        print(None)
    else:
        print(round(result, 5))


def divide_safe(num1_str, num2_str):
    """Returns num1/num2 if the input is valid, else None."""

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)

    except ValueError:
        return None

    try:
        return num1 / num2

    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    main()
