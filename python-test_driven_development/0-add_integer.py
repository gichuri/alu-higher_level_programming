#!/usr/bin/python3
"""
This module describes a method to add two integers
"""


def add_integer(a, b=98):
    '''
    add two integers

    '''
    if type(a) or type(b) == float:
        a = int(a)
        b = int(b)
    elif type(a) is not int:
        raise TypeError("{} must be an integer".format(a))
    elif type(b) is not int:
        raise TypeError("{} must be an integer".format(b))
    else:
        print a+b
