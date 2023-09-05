#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """Return integer sum of a and b

    Float arguments are casted before addition is performed.

    Raises:
        TypeError: if a or b is not integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
