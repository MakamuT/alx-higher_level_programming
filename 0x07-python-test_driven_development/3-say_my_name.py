#!/usr/bin/python3
"""
say_my_name module
prints pin names

"""


def say_my_name(first_name, last_name=""):
    """Return: the first and last name
    Args: argument
    param1: type str first name
    param2: type str last name
    Raise: raise a TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
