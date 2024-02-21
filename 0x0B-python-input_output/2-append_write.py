#!/usr/bin/python3
"""Defines file-append function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    Args:
        filename - name of the file to write to.
        text(str) - the string to write
    Returns:
        the number of characters added:
        """
        with open(filename, "a", encoding="UTF8") as f:
            return f.write(text)
