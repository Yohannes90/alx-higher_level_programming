#!/usr/bin/python3
"""this module inherits list class"""


class MyList(list):
    """This class inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
