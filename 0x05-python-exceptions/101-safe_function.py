#!/usr/bin/python3
""" a function that executes a function safely """
import sys


def safe_function(fct, *args):
    """
    safe_function - executes a function safely
    Args:
        fct: a function
        args: arguments
    Return:
        result of function execution
    """
    try:
        return (fct(*args))
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
