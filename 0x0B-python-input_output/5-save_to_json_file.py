#!/usr/bin/python3
"""Module containing a function that write object to file"""

import json


def save_to_json_file(my_obj, filename=""):
    """object to textfile by json represention"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
