#!/usr/bin/python3
"""Module containing a function to read from file"""


def read_file(filename=""):
    """Reads from a file

    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
