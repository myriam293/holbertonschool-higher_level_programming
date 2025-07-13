#!/usr/bin/python3
"""Write a class Student that defines a student
by public instance attributes."""


class Student:
    """Defines a student by: first_name, last_name, age."""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
