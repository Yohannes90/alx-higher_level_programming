#!/usr/bin/python3
"""Describes Student"""


class Student:
    """Representation of Student"""
    def __init__(self, first_name, last_name, age):
        """Initalizes student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dicionary representatuon of student object"""
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:
            json (dict): to replace with
        """
        for key, value in json.items():
            setattr(self, key, value)
