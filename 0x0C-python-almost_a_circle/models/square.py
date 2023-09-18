#!/usr/bin/python3
""" This module contains a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initalize sqare object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of rectangle object"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                          self.x,
                                                          self.y,
                                                          self.width))

    @property
    def size(self):
        """Square size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Square size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Assigns/updates an argument to each square attribute'''
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of square object"""
        return {'id': getattr(self, "id"),
                'x': getattr(self, "x"),
                'size': getattr(self, "size"),
                'y': getattr(self, "y")}
