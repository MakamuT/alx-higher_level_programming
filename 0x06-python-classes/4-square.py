#!/usr/bin/python3

"""Square class"""


class Square():
    """Define square"""

    def __init__(self, size=0):
        """Set attributes for the square
        Args:
            size (int): one side
        """
        self.size = size

    @property
    def size(self):
        """Get and set of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns area of square"""
        return self.__size ** 2
