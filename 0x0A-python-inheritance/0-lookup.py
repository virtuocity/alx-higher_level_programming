#!/usr/bin/python3
"""Details of an object"""


def lookup(obj):
    """a function that returns the list of available
    attributes and methods of an object
    Args:
    obj
    Returns:
    object attributes
    """
    return (dir(obj))
