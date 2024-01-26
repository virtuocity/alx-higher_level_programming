#!/usr/bin/python3
"""a function that tests first name and last name
input
"""


def say_my_name(first_name, last_name=""):
    """say_my_name - print first name and last name
       args:
            fisrt_name: first name
            last_name: last name
        Return: print first name and last name
    """
    if first_name is None or type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
