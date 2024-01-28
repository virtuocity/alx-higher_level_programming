#!/usr/bin/python3
import sys
""" a function that prints an integer """


def safe_print_integer_err(value):
    """ safe_print_integer_err - prints integer
    Args:
        value: can be any type (integer, string,
        etc.)
    Return:
        True if value has been correctly printed
        (it means the value is an integer)
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
