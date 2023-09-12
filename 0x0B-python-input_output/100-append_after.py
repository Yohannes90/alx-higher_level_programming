#!/usr/bin/python3
"""Contains function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    '''inserts a line of text to a file,
    after each line containing a specific string'''
    with open(filename, 'r+', encoding="utf-8") as f:
        lines_list = f.readlines()
        i = 0
        for line in lines_list:
            if line.find(search_string) != -1:
                lines_list.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.write("".join(lines_list))
