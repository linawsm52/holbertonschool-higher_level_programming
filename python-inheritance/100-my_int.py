#!/usr/bin/python3
"""
This module defines a custom integer class MyInt
with inverted equality operators.
"""


class MyInt(int):
    """
    MyInt is a rebel class that inverts == and != operators.
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
