#!/usr/bin/python3
"""Write text to a file"""


def write_file(filename="", text=""):
    if filename is None or text is None:
        return
    n = 0
    with open(filename, "w", encoding="utf-8") as f:
        n = f.write(text)
    return (n)