#!/usr/bin/python3
"""
Module 1-write_file
Writes a string to a UTF-8 text file and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns
    the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
