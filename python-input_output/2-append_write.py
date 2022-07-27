#!/usr/bin/python3

"""function to append the contents of file"""


def append_write(filename="", text=""):

    '''
    :param filename
    :param text
    :return: characters added
    '''
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text))
