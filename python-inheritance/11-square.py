#!/usr/bin/python3
"""Define a class Square that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): Size of the square's side.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
