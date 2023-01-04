#!/usr/bin/python3
""" adds two ints or floats"""
def add_integer(a, b=98):
    if a is None or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)    
