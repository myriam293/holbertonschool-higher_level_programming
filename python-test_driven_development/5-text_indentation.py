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

    result = ""
    buffer = ""

    for char in text:
        if char in ".?:":
            print(buffer.strip() + char)
            print()
            buffer = ""
        else:
            buffer += char

    if buffer.strip():
        print(buffer.strip())
