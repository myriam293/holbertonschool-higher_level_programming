#!/usr/bin/python3
"""Module that defines add_integer function."""
def add_integer(a, b=98):
    """Adds 2 integers.
    
    Args:
        a: First number.
        b: Second number (defaults to 98).
    
    Returns:
        The sum of a and b, casted to integers.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
