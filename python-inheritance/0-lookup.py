#!/usr/bin/python3
"""Module that defines a function to list available attributes and methods."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
