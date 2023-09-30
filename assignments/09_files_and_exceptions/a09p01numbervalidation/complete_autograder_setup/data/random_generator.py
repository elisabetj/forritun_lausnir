#!/usr/bin/python3
import random
import sys
import string

random.seed(sys.argv[-1])  # Using the first argument for seeding.


def random_string(length):
    letters = [chr(i) for i in range(32, 127)]
    return "".join(random.choices(letters, k=length))


def random_integer(min_int, max_int):
    return random.randint(min_int, max_int)


def random_float_with_decimals(min_x, max_x, decimals):
    return round(random.uniform(min_x, max_x), decimals)


def random_sci_notation():
    choice = random.choice(["standard", "positive_exponent", "exponent_only"])

    base = random.uniform(1, 9.99)
    exponent = random.randint(-99, 99)

    if choice == "standard":
        return "{:.2e}".format(base * (10**exponent))
    elif choice == "positive_exponent":
        if exponent > 0:
            return "{:.2f}e+{}".format(base, exponent)
        else:
            return "{:.2f}e{}".format(base, exponent)
    elif choice == "exponent_only":
        return "e{}".format(exponent)


def random_leading_zero_float(min_x, max_x, has_leading_zero=True):
    value = random.uniform(min_x, max_x)
    if has_leading_zero:
        return "0{:.2f}".format(value)
    else:
        return "{:.2f}".format(value)


def random_string_float():
    base_float = "{:.2f}".format(random.uniform(1, 9999.99))
    if random.choice([True, False]):
        base_float = "-" + base_float
    insert_pos = random.randint(
        1, len(base_float) - 3 if base_float[0] != "-" else len(base_float) - 2
    )  # Avoiding the last two digits (after the decimal) and consider negative sign
    random_char = random.choice(
        string.ascii_letters + string.digits + string.punctuation
    )
    return base_float[:insert_pos] + random_char + base_float[insert_pos:]


def random_string_integer(length):
    base_int = random_integer(
        1, 10**length - 1
    )  # This generates an integer with the given length
    if random.choice([True, False]):
        base_int = -base_int
    s = str(base_int)
    insert_pos = random.randint(1, len(s) - 1)  # Position to insert character
    random_char = random.choice(
        string.ascii_letters + string.digits + string.punctuation
    )
    return s[:insert_pos] + random_char + s[insert_pos:]


def no_leading_decimal_zero_int(min_x, max_x):
    value = random.randint(min_x, max_x)
    s = f"{int(value)}."
    return s


def infinity(inf_or_neg_inf):
    if inf_or_neg_inf:
        return "inf"
    else:
        return "-inf"


def random_float_with_underscores(min_x, max_x, decimals):
    base_float = "{:.{}f}".format(random.uniform(min_x, max_x), decimals)
    num_underscores = random.randint(
        1, len(base_float) // 2
    )  # Just a heuristic for the number of underscores.
    for _ in range(num_underscores):
        insert_pos = random.randint(1, len(base_float) - 1)
        base_float = base_float[:insert_pos] + "_" + base_float[insert_pos:]
    return base_float


data_type = sys.argv[1]  # Using the second argument to determine the data type.

if data_type == "string":
    length = int(sys.argv[2])
    print(random_string(length))
elif data_type == "integer":
    min_int = int(sys.argv[2])
    max_int = int(sys.argv[3])
    print(random_integer(min_int, max_int))
elif data_type == "float":
    min_x = float(sys.argv[2])
    max_x = float(sys.argv[3])
    decimals = int(sys.argv[4])
    print(random_float_with_decimals(min_x, max_x, decimals))
elif data_type == "sci_notation":
    print(random_sci_notation())
elif data_type == "leading_zero":
    min_x = float(sys.argv[2])
    max_x = float(sys.argv[3])
    has_leading_zero = bool(int(sys.argv[4]))
    print(random_leading_zero_float(min_x, max_x, has_leading_zero))
elif data_type == "string-float":
    print(random_string_float())
elif data_type == "string-integer":
    length = int(sys.argv[2])
    print(random_string_integer(length))
elif data_type == "no_leading_decimal_zero_int":
    min_x = float(sys.argv[2])
    max_x = float(sys.argv[3])
    print(no_leading_decimal_zero_int(min_x, max_x))
elif data_type == "infinity":
    inf_or_neg_inf = bool(int(sys.argv[2]))
    print(infinity(inf_or_neg_inf))
elif data_type == "NaN":
    print("NaN")
elif data_type == "dot":
    print(".")
elif data_type == "multiple_dots":
    print("1..1")
elif data_type == "float_underscore":
    min_x = float(sys.argv[2])
    max_x = float(sys.argv[3])
    decimals = int(sys.argv[4])
    print(random_float_with_underscores(min_x, max_x, decimals))
