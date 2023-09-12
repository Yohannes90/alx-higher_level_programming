#!/usr/bin/python3
"""Module containing a function that create py object from json"""

import json


def load_from_json_file(filename=""):
    """Create a Python object from a json file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
