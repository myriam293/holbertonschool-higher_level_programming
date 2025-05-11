#!/usr/bin/python3
"""This module defines a Square class with validated size and area method."""


class Square:
    """Represents a square with size validation and area computation."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): Size of the square, must be an integer >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size
