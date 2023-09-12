#!/usr/bin/python3
"""Module containing a function to appends string"""


def append_write(filename="", text=""):
    """return the number of chars added to file from text"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
