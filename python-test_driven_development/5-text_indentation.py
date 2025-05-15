#!/usr/bin/python3
"""A function that prints a text with 2 new lines after '.', '?' or ':'."""


def text_indentation(text):
    """Prints text with two new lines after '.', '?' or ':'.

    Args:
        text (str): The input text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length:

        while i < length and text[i] == ' ':
            i += 1

        while i < length and text[i] not in ".:?":
            print(text[i], end='')
            i += 1

        if i < length and text[i] in ".:?":
            print(text[i], end='')
            print("\n")
            i += 1
