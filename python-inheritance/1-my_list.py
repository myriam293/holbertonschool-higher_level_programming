#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """The puts sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
