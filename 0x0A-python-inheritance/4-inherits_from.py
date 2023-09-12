#!/usr/bin/python3
"""Checks whether object is an instance of a class
that inherited from specified class """


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class or false"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
