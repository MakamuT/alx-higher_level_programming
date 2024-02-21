#!/usr/bin/python3
"""Defines a writing function on a file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters writtten
    Args:
        filename - name of the file to write to.
        text(str) - the string to write
    Return:
        Number of charater written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
