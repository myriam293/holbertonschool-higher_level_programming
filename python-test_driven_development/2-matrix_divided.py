#!/usr/bin/python3
"""This module provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number and returns a new matrix.

    Each element in the matrix is divided by `div`, and the result is
    rounded to 2 decimal places. The original matrix remains unmodified.

    Args:
        matrix (list of lists): A non-empty matrix (list of lists) containing
            only integers or floats. All rows must be of the same length.
        div (int or float): The number to divide each matrix element by.
            Must be a non-zero number.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not all the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix where each element is the original element
        divided by `div`, rounded to 2 decimal places.

    Example:
        >>> matrix_divided([[1, 2], [3, 4]], 2)
        [[0.5, 1.0], [1.5, 2.0]]
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
