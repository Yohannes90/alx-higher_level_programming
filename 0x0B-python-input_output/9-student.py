#!/usr/bin/python
"""Describes Student"""


class Student:
    """Representation of Student"""
    def __init__(self, first_name, last_name, age):
        """Initalizes student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dicionary representatuon of student object"""
        return self.__dict__
