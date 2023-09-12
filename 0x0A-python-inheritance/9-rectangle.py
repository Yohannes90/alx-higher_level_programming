#!/usr/bin/python3
'''Defines a rectangle class'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''This class represents rectangle class'''
    def __init__(self, width, height):
        """Initalize rectangle object"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """String representation of rectangle object"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
