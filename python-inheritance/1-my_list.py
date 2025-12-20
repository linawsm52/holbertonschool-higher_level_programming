#!/usr/bin/python3
"""Module that defines MyList class"""


class MyList(list):
    """Custom list class that can print itself sorted"""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original"""
        print(sorted(self))
