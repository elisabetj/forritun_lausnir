def decimal_to_binary(decimal: int) -> str:
    """Converts an integer from decimal to its binary representation."""

    if decimal == 0:
        return "0"

    binary_string = ""
    quotient = decimal
    while quotient > 0:
        remainder = quotient % 2
        binary_string = str(remainder) + binary_string
        quotient = quotient // 2

    return binary_string
