#!/usr/bin/python3
""" Module that contains a function that appends to a text file
"""


def append_write(filename="", text=""):

    '''
    :param filename
    :param text
    :return: characters added
    '''
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text))
