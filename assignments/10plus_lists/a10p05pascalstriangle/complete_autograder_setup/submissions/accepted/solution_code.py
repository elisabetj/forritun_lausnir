def main():
    height = int(input())
    new_row = []
    for _ in range(height):
        new_row = make_new_row(new_row)
        print(new_row)


def make_new_row(old_row: list) -> list:
    """Makes a new row in the Pascal triangle given the previous row."""

    new_row = [1]
    length = len(old_row)
    if length > 0:
        for i in range(0, length - 1):
            new_row.append(old_row[i] + old_row[i + 1])
        new_row.append(1)
    return new_row


if __name__ == "__main__":
    main()
