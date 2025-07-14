#!/usr/bin/python3
"""Module that converts CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(filename):
    """Reads a CSV file and writes its content as JSON to 'data.json'
    Returns True if successful, otherwise False
    """
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        return True

