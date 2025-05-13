#!/usr/bin/python3
"""This module provides a function to add two integers."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an int or float.

    Returns:
        int: The sum of a and b as an integer.
    """
def add_integer(a, b=98):
    if type(a)!= int and type(a)!= float:
        raise TypeError("a must be an integer")
    if type(b)!= int and type(b)!= float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

