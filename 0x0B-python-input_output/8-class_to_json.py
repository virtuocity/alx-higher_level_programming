#!/usr/bin/python3
""" Class to JSON"""


def class_to_json(obj):
    """class_to_json - turn object into JSON
       Args:
            @obj: instance of a class
        Return:
            JSON representation of an object
    """
    obj_dict = {}
    if hasattr(obj, '__dict__'):
        return (obj.__dict__)
    return (obj_dict)
