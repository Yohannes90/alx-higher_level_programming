#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """This class represents base geometry class"""
    def area(self):
        """to be implemented area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """valideates a value as an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
