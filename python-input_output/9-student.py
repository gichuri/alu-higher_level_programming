#!/usr/bin/python3
"""class with public instance and json rep for obj"""


class Student:

    """instantiate class"""
    def __init__(self, first_name, last_name, age):
        """method to iniate class object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """returns the dictionary representation of class object"""
        return self.__dict__
