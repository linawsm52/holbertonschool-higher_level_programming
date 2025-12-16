#!/usr/bin/python3
"""Divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div, rounded to 2 decimal places."""
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) for row in matrix) or
            any(row == [] for row in matrix) or
            any(any(not isinstance(x, (int, float)) for x in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
