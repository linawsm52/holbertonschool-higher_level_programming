#!/usr/bin/python3
"""0-add_integer module."""


def add_integer(a, b=98):
    """Adds 2 integers."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    if a != a or a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if b != b or b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
