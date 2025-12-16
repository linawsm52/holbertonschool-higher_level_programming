#!/usr/bin/python3
"""
Module that contains add_integer function
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    a and b must be integers or floats.
    If they are floats, they are casted to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
