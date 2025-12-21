#!/usr/bin/python3
"""Divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div and rounded to 2 decimals."""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(row for row in matrix) or
            not all(isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            value = round(x / div, 2)
            if value == 0:
                value = 0.0
            new_row.append(value)
        new_matrix.append(new_row)

    return new_matrix
