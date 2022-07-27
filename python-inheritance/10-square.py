#!/usr/bin/python3

"""new class square that extends the super class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''instatiation of new class square'''

    def __init__(self, size):
        self.__size = size
        super().integer_validator('size', size)

    def area(self):
        """override method in super()"""

        return self.__size * self.__size
