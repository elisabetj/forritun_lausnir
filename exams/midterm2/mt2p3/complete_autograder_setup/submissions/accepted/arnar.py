#!/usr/bin/python3

def read_matrix(rows, columns):
    result = []
    for row in range(rows):
        result_row = []
        for col in range(columns):
            result_row.append(int(input()))
        result.append(result_row)
    return result

def add_matrices(lhs, rhs):
    """
    Note: lhs and rhs mean left/right hand side
    Asserts are added for sanity checks
    Cannot add matrices with different dimensions
    """
    assert len(lhs) == len(rhs)
    result = []
    for row in range(len(lhs)):
        assert len(lhs[row]) == len(lhs[0])
        assert len(lhs[row]) == len(rhs[row])
        result_row = []
        for col in range(len(lhs[row])):
            result_row.append(lhs[row][col] + rhs[row][col])
        result.append(result_row)
    return result

def main():
    ROWS = 2
    COLUMNS = 3
    lhs = read_matrix(ROWS, COLUMNS)
    rhs = read_matrix(ROWS, COLUMNS)
    print(lhs)
    print(rhs)
    print(add_matrices(lhs, rhs))

if __name__ == "__main__":
    main()
