#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Prints a name

    Args:
        first_name (str): first name
        last_name (str, optional): last_name. Defaults to "".

    Raises:
        TypeError: if first name is not str
        TypeError: if last name is not str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is", first_name)
    else:
        print("My name is", first_name, last_name)
