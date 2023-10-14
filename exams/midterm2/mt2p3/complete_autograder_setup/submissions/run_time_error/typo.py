from typing import List

ROWS, COLUMNS = 2, 3


def main() -> None:
    A = get_matrix()
    B = get_matrix()
    C = add_matrices(A, B)
    display_output(A, B, C)


def get_matrix(
    rows: int = ROWS,
    columns: int = COLUMNS,
) -> List[List[int]]:
    matrix = []
    for _ in range(rows):
        line = [int(input()) for _ in range(columns)]
        matrix.append(line)

    return matrix


def add_matrices(
    A: List[List[int]],
    B: List[List[int]],
) -> List[List[int]]:
    rows = len(A)
    assert len(B) == rows
    if rows:
        columns = len(A[0])
        for line in A + B:
            assert len(line) == columns

    C = []
    for row in range(rows):
        line = []
        for column in range(columns):
            a = A[row][column]
            b = B[row][column]
            c = a + B
            line.append(c)

        C.append(line)

    return C


def display_output(
    A: List[List[int]],
    B: List[List[int]],
    C: List[List[int]],
) -> None:
    print(A)
    print(B)
    print(C)


if __name__ == "__main__":
    main()
