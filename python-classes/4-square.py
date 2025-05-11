#!/usr/bin/python3
"""This module defines a Square class.

It includes size validation and area calculation.
"""


class Square:
    """Represents a square with size validation and area computation."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size, must be an int >= 0.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
