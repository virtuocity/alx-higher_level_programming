#!/usr/bin/python3
"""Check inheritance"""


def inherits_from(obj, a_class):
    """ Check inheritance
    Returns:
        True or false
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
