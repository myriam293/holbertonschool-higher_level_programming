#!/usr/bin/python3
"""Module that provides basic serialization
and deserialization functionality"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data: A Python Dictionary with data.
        filename: The filename of the output
        JSON file. Replaces the file if it exists.
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(data))


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file into a Python dictionary.

    Args:
        filename: The filename of the input JSON file.

    Returns:
        A Python Dictionary with the deserialized JSON data.
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        return json.loads(file.read())
