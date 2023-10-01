def main():
    height = int(input())
    row = [1]
    for _ in range(height):
        print(row)
        row = make_new_row(row)


def make_new_row(old_row: list) -> list:
    """Makes a new row in the Pascal triangle given the previous row."""

    assert len(old_row) > 0

    new_row = [1]
    for i in range(0, len(old_row) - 1):
        new_row.append(old_row[i] + old_row[i + 1])
    new_row.append(1)

    return new_row


if __name__ == "__main__":
    main()
