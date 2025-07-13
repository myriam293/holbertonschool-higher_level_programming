#!/usr/bin/python3
"""Write a class Student that defines a student by public attributes and methods."""


class Student:
    """Defines a student by: first_name, last_name, age."""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only those attributes are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(type(e) is str for e in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Assumes json is a dictionary with keys as public attribute names.
        """
        for key, value in json.items():
            self.__dict__[key] = value
