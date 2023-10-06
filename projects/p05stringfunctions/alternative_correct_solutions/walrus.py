#!/usr/bin/python3

QUIT = "q"
COLLECT_DIGITS = "c"
INVERSE_CASE = "i"
TO_HEX = "h"


def main():
    """Accepts input, calls the appropriate functions,
    and displays the result."""

    while (option := input()) != QUIT:
        a_str = input()
        if option == COLLECT_DIGITS:
            digits = collect_digits(a_str)
            print(digits)
        elif option == INVERSE_CASE:
            reversed_str = inverse_case(a_str)
            print(reversed_str)
        elif option == TO_HEX:
            an_int = int(a_str)
            hex_str = to_hex(an_int)
            print(hex_str)


def collect_digits(a_str: str) -> str:
    """Returns a string containing all the digits from the given string."""

    digits = ""
    for letter in a_str:
        if letter.isdigit():
            digits += letter

    return digits


def inverse_case(a_str: str) -> str:
    """Returns a string in which upper case letters in the given string are replaced with lower case, and vice versa."""

    inversed_str = ""
    for char in a_str:
        if char.islower():
            inversed_str += char.upper()
        else:
            inversed_str += char.lower()

    return inversed_str


def to_hex(an_int: int) -> str:
    """Returns a string which is the hexadecimal respresentation of the given integer."""
    if an_int == 0:
        hex_str = "0"
    else:
        hex_str = ""
        quotient = an_int
        while quotient > 0:
            remainder = quotient % 16
            hex_str = to_hex_letter(remainder) + hex_str
            quotient = quotient // 16

    return hex_str


def to_hex_letter(remainder: int) -> str:
    """Maps an integer in the range 0-15 to a hexadecimal letter."""
    if remainder < 10:
        return str(remainder)
    else:
        return chr(remainder + 55)  # A = 65, B = 56, etc.


if __name__ == "__main__":
    main()
