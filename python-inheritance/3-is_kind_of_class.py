#!/usr/bin/python3
"""Module that checks if an object is an instance of a class or inherited from it."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclasses."""
    return isinstance(obj, a_class)
