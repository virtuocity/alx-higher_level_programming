#!/usr/bin/python3
"""Write text to a file"""


def write_file(filename="", text=""):
    """
    write_file - write  text to file
    Args:
        @filename: file to be opened for writing
        @text: text to be input to file
    Return : number of characters writtent to file i.e
        the return value of the write() function
    """
    # check if file or text args is absent/empty?
    if filename is None or text is None:
        return 0
    n = 0
    with open(filename, "w", encoding="utf-8") as f:
        n = f.write(text)
    return (n)
