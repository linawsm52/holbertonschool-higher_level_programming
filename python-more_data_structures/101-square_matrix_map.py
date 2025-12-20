#!/usr/bin/python3
"""Squares all values of a matrix using map."""


def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
