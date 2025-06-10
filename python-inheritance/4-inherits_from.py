#!/usr/bin/python3
"""A function that returns True if the object is an instance of
a class that inherited (directly or indirectly)
from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        issubclass(a_class, obj):
        return True
    return False
