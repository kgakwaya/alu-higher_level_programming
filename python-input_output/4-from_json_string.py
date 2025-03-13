#!/usr/bin/python3
"""
This module provides a function to convert a JSON string to a Python object.
"""


import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.
    Args:
        my_str (str): The JSON string to be converted.
    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
