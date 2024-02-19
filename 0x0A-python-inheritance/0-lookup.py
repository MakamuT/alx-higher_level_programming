#!/usr/bin/python3
"""module lookup the list of available attributes and methods of an object:"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return sorted(dir(obj))
