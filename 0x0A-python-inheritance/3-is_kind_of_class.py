#!/usr/bin/python3
"""Checks whether object is an instance of a class
or an inherited class """


def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance of a class or false"""
    return (isinstance(obj, a_class))
