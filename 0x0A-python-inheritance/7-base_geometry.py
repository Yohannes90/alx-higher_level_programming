#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """This class represents base geometry class"""
    def area(self):
        """to be implemented area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """valideates a value as an integer and greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
