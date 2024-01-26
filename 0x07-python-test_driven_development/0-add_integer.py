#!/usr/bin/python3
"""
    function to add two integers
    Args:
    a and b and return sum
"""


def add_integer(a, b=98):
    """ add_integer - adds two ints or floats
    arguments:
        a: one positional argument
            it must be an int and not None
        b: optional argument b must also be an integer
    Return: sum of a and b
    """
    if a is None or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (a + 1) == a:
        raise OverflowError("a is too large")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if (b + 1) == b:
        raise OverflowError("b is too large")
    a = int(a)
    b = int(b)
    return (a + b)
