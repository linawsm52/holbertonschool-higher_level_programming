#!/usr/bin/python3
"""Prints a formatted name."""


def say_my_name(first_name=None, last_name=""):
    """Prints My name is <first_name> <last_name>."""
    if first_name is None:
        raise TypeError(
            "say_my_name() missing 2 required positional arguments: "
            "'first_name' and 'last_name'"
        )

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
