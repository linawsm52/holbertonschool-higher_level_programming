#!/usr/bin/python3
"""
Module 2-append_write
Appends a string to a UTF-8 text file and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF-8 text file and returns
    the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
