#!/usr/bin/python3

"""A rectangle class that inhert from Geometry 
        more projects on classes and objects"""
class Rectangle(BaseGeometry):
        '''instatiating Rectangle object'''

        def __init__(self, width, height):
            self.__width = width
            self.__height = height
            super().integer_validator('width', self.__width)
            super().integer_validator('height', self.__height)
