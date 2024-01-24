#!/usr/bin/python3
""" safe division of integers"""


def safe_print_division(a, b):
    div = 0
    try:
        div = a/b
        return div
    except ZeroDivisionError:
        div = None
        return div
    finally:
        print("Inside result: {}".format(div))
