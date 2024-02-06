#!/usr/bin/python3
""" function to read a file """


def read_file(filename=""):
    """ 0-read_file - read contents of a file
    Args:
        @filename: file to be read
    Return : content of file to stdout
    """
    with open(filename,  encoding='utf-8') as f:
        print(f.read(), end="")
