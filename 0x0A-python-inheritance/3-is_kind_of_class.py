#!/usr/bin/python3
"""is same class or sublclass"""


def is_kind_of_class(obj, a_class):
    """the object isan instance of, or if the object is an
    instance of a class that inherited from the class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
