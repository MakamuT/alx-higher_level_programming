#!/usr/bin/python3
"""
print_square module
print a square using #

"""


def print_square(size):
    """Return: sqaure of #
    Args: argument
    Param1: size of the square
    Raises: raise TypeError or ValueError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print('#', end="") for j in range(size)]
        print("")
