#!/usr/bin/python3
""" Append to a file"""


def append_write(filename="", text=""):
    """
    write_file - write  text to file
    Args:
        @filename: file to be opened for writing
        @text: text to be input to file
    Return : number of characters writtent to file i.e
        the return value of the write() function
    """
    # check if file or text args is absent/empty?
    n = 0
    with open(filename, "a", encoding="utf-8") as f:
        n = f.write(text)
    return (n)
