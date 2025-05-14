#!/usr/bin/python3
"""A function that prints a text with 2 new lines after '.', '?', or ':'."""


def text_indentation(text):
    """Print text with two new lines after '.', '?', and ':'.

    Args:
        text (str): The input text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        if text[c] in ".?:":
            print(text[c])
            print()
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
        else:
            print(text[c], end="")
            c += 1
