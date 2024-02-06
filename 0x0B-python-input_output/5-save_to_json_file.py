#!/usr/bin/python3
""" save to JSON file """


import json
def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - writes an Object to a text file, using\
    a JSON representation
    Args:
        my_obj - object to be serialized
        filename - filename to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
