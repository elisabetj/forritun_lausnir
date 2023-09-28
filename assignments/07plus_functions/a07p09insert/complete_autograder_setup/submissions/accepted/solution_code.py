def insert_at(sequence: str, index: int, element: str) -> str:
    """Inserts an element at the specified location in a sequence and returns the updated sequence."""

    return sequence[:index] + element + sequence[index:]


if __name__ == "__main__":
    print(insert_at(input(), int(input()), input()))
