#!/usr/bin/python3
'''Defines a square class'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''This class represents square class'''
    def __init__(self, size):
        """Initalize square object"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.size ** 2

    def __str__(self):
        """String representation of rectangle object"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
