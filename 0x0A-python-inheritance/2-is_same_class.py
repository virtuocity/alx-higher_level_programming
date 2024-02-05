#!/usr/bin/python3
""" Is same class?"""


def is_same_class(obj, a_class):
    """Check if an object belongs to a class
    Args:
    @obj: object to check
    @a_class: Class
    Returns:
    True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
