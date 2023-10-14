#!/usr/bin/python3

ROWS = 2
COLS = 3

def main():
    matrix1 = fill_matrix()
    matrix2 = fill_matrix()
    print(matrix1)
    print(matrix2)
    matrix3 = add_matrices(matrix1, matrix2)
    print(matrix3)
    

def fill_matrix():
    '''Returns a matrix with dimension ROWS,COLS, filled with data input by the user.'''
    
    matrix = []
    for _ in range(ROWS):
        row = []
        for _ in range(COLS):
            elem = int(input())
            row.append(elem)
        matrix.append(row)
    
    return matrix


def add_matrices(matrix1, matrix2):
    '''Returns a matrix with dimension ROWS,COLS, which is the sum of matrix1 and matrix2.'''
    
    matrix_sum = []
    return matrix_sum


if __name__ == "__main__":
    main()