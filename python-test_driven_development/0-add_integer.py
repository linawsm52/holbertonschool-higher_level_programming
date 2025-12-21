#!/usr/bin/python3
"""0-add_integer module."""


def add_integer(a, b=98):
    """Return the sum of two integers."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if a != a or a in (float("inf"), float("-inf")):
        raise TypeError("a must be an integer")
    if b != b or b in (float("inf"), float("-inf")):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
