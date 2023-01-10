#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    if filename is None:
        return
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
