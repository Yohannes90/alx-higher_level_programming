#!/usr/bin/python3
"""Checks whether object is an instance of a class"""


def is_same_class(obj, a_class):
    """Return true if object is instance of the class, or false"""
    return type(obj) is a_class
