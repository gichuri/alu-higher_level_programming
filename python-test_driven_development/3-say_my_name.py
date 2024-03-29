#!/usr/bin/python3
""" print out a person's name """


def say_my_name(first_name, last_name=""):
    """check whether each
    paremeter is type string"""
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
