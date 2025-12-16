#!/usr/bin/python3
"""Defines a function that adds two integers."""

def add_integer(a, b=98):
    """Return the addition of a and b as integers.

    a and b must be integers or floats, otherwise raise a TypeError.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN check
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # Infinity / overflow check
    if a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
