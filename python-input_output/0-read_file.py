#!/usr/bin/python3
"""
Module 0-read_file
Reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
