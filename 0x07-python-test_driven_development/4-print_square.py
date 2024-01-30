#!/usr/bin/python3
""" print a square """


def print_square(size):
    """ print_square - print a square
        Args:
            size: size of a side of square
        Return:
            Print square with "#"
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            if j != (size - 1):
                print("{}". format("#"), end="")
            else:
                print("{}".format("#"))
