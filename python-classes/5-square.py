#!/usr/bin/python3
"""This module defines a Square class with size validation and printing."""


class Square:
    """Represents a square with size validation and print capability."""

    def __init__(self, size=0):
        """Initialize the square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size (must be >= 0).
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the square's area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
