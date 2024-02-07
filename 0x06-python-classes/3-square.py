#!/usr/bin/python3
"""Square area"""


class Square():
    """Define square."""
    def __init__(self, size=0):
        """attributes for the Square object
        Args:
            size (int): one side
        Raises:
            TypeError: if size is not given as an integer.
            [O
            ValueError: if size is less than 0.
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns area of square"""
        return self.__size ** 2
