#!/usr/bin/python3
"""Define a Student class with a method
to retrieve a dictionary representation."""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Instantiate with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are
        retrieved. Otherwise, all attributes are retrieved.
        """
        if (isinstance(attrs, list)
                and all(type(attr) is str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
