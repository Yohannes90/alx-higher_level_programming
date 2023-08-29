#!/usr/bin/python3

""" Defining a class Square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)) or not all(n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(n, int) for n in value) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        size = self.__size
        position = self.__position
        if size == 0:
            print("")
            return
        for row in range(position[1]):
            print("")
        for row in range(size):
            for col in range(position[0]):
                print(" ", end="")
            for coll in range(size):
                print("#", end="")
            print("")
