#!/usr/bin/python3
"""Module that returns Pascal’s triangle of n"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = []
        for j in range(i + 1):
            if j != 0 and j != i:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            else:
                row.append(1)
        triangle.append(row)
    return triangle
