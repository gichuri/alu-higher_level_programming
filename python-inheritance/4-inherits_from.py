#!/usr/bin/python3

''' verify if object 
        is intance of class'''


def inherits_from(obj, a_class):

    '''use builtin issubclass'''

    if type(obj) == a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
