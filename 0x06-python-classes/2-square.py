#!/usr/bin/python3
"""a Class Square defined by a sqaure"""


class Square:
    """Private instance attribute: size
    Instantiate size: def __init__(self, size=0):"""

    def __init__(self, size=0):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
