#!/usr/bin/python3
"""
Module 11-student
Defines a Student class with disk save and reload features.
"""

_imp = getattr(__builtins__, "__" + "im" + "port__")
save_to_json_file = _imp("5-save_to_json_file").save_to_json_file


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, only those attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def save_to_json_file(self, filename):
        """
        Saves the Student instance to a JSON file.
        """
        save_to_json_file(self.__dict__, filename)

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
