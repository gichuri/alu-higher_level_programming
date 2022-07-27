#!/usr/bin/python3



class Rectangle(BaseGeometry):
        '''instatiating Rectangle object'''

        def __init__(self, width, height):
            self.__width = width
            self.__height = height
            super().integer_validator('width', self.__width)
            super().integer_validator('height', self.__height)

        def area(self):
            '''this should override the area method in super()'''

            return self.__width * self.__height

        def __str__(self):
            ''' return a specified str'''

            return "[Rectangle] {}/{}".format(self.__width, self.__height)
