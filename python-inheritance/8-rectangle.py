#!/usr/bin/python3

"""new class recangle that
        extends the class geometry"""


class Rectangle(BaseGeometry):
        '''instatiating Rectangle object'''

        def __init__(self, width, height):
            self.__width = width
            self.__height = height
            super().integer_validator('width', self.__width)
            super().integer_validator('height', self.__height)
