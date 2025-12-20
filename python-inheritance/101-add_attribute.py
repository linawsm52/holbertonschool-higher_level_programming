#!/usr/bin/python3
"""Defines a function to add an attribute to an object."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible."""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
