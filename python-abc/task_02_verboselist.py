#!/usr/bin/python3
"""Create a class named VerboseList that
extends the Python list class."""


class VerboseList(list):
    """VerboseList prints a notification
    message when items are added or removed."""

    def append(self, value):
        """Print a message when an item is added using append."""
        print(f"Added [{value}] to the list.")
        super().append(value)

    def extend(self, value):
        """Print a message when the list is extended."""
        print(f"Extended the list with [{len(value)}] items.")
        super().extend(value)

    def remove(self, value):
        """Print a message when an item is removed using remove."""
        print(f"Removed [{value}] from the list.")
        super().remove(value)
