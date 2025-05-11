#!/usr/bin/python3
"""This module defines a function to replace an element in a copied list."""


def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position.

    Args:
        my_list (list): The original list.
        idx (int): The index to replace.
        element (any): The new element to insert.

    Returns:
        list: A new list with the element replaced if index is valid;
              otherwise, the original list unchanged.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    copy = my_list.copy()
    copy[idx] = element
    return copy
