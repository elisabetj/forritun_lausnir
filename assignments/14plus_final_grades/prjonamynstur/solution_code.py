#!/usr/bin/python3

YARN_USAGE = {
    ".": 20,  # Garter stitch.
    "O": 10,  # Yarn over.
    "\\": 25,  # Slip one stitch, knit next stitch and pass slip stitch over knit stitch.
    "/": 25,  # Knit two stitches together.
    "A": 35,  # Knit three stitches together.
    "^": 5,  # No stitch.
    "v": 22,  # Purl on right side, knit on wrong side.
}


def main():
    recipe = get_recipe()
    total_yarn = calculate_yarn_usage(recipe)
    print(total_yarn)


def get_recipe():
    number_of_rows, number_of_columns = map(int, input().split())
    recipe = [input() for _ in range(number_of_rows)]
    assert all(len(row) == number_of_columns for row in recipe)
    return recipe


def calculate_yarn_usage(recipe) -> int:
    total_yarn = sum(YARN_USAGE[symbol] for row in recipe for symbol in row)
    return total_yarn


if __name__ == "__main__":
    main()
