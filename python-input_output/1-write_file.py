#!/usr/bin/python3

"""
create new file and return characters written
"""


def write_file(filename="", text=""):
    '''
    open file or create new file
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
