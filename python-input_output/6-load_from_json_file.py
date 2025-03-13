#!/usr/bin/python3
"""
This module provides function to loadPython object from jSON file.
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.
    Args:
        filename (str): The name of the JSON file to read from.
    Returns:
        object: The Python object created from the JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
