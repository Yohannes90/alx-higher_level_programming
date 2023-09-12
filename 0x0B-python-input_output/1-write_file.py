#!/usr/bin/python3
"""Module containing a function to write on file"""


def write_file(filename="", text=""):
    """return the number of chars written to file from text"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
