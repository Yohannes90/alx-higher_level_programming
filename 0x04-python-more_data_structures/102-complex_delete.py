#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_list = list(a_dictionary.keys())
    for key in keys_list:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
