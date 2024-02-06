#!/usr/bin/python3
"""
Load from json file, a function that creates an Object from a “JSON file"
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - a function that creates an Object from a “JSON file”
    Args:
        @filename: json file
    Return:
        object from json file
    """
    with open(filename, "r", encoding="utf-8") as f:
        # return deserealized object
        return (json.load(f))
