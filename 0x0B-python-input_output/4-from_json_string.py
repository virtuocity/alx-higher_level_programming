#!/usr/bin/python3
"""a function that returns an object (Python data structure)
    represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    from_json_string-return object from string
    Args:
        @my_str: string input to form object
    Return: object
    """
    return (json.loads(my_str))
