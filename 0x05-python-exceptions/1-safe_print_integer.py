#!/usr/bin/python3
""" Check argument type using exceptions"""


def safe_print_integer(value):
    """
    safe_print_integer - Check argument type using exceptions
    Args:
        @value: value to check if is integer
    Return:
        True or false if is int or if
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
