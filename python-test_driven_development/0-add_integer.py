#!/usr/bin/python3
"""This module provides a function to add two integers."""


def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), default is 98.

    Returns:
        The integer addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
