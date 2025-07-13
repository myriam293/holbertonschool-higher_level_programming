#!/usr/bin/python3
"""Return the dictionary description with simple
data structure for JSON serialization."""
def class_to_json(obj):
    """Return the dictionary description for
    JSON serialization of an object."""
    return obj.__dict__
