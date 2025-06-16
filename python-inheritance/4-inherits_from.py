#!/usr/bin/python3
"""A function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a subclass of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare inheritance with.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
