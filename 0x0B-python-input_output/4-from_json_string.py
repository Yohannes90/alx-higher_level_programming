#!/usr/bin/python3
"""Module containing a function from json string"""


import json


def from_json_string(my_str):
    """return object represented by a json string"""
    return json.loads(my_str)
