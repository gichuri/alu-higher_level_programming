#!/usr/bin/python3


'''verifying if object belings
    to a specified class'''


def is_same_class(obj, a_class):
    '''use builtin type to check obj instance'''

    if type(obj) == a_class:
        return True
    else:
        return False
