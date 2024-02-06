#!/usr/bin/python3
"""Convert object to JSON"""


import json


def to_json_string(my_obj):
    """
    to_json_string - serialize an object i.e the string representaion
    of an object
    Args:
        @my_obj: return string of this
    Return:
        string representaion of an object
    """
    return (json.dumps(my_obj))
