#!/usr/bin/python3
"""Module for serializing and deserializing a dictionary using XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary into XML and save to the given filename"""
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML data from a file and return a dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
