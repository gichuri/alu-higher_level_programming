#!/usr/bin/python3



'''
class square
defines a square
'''


class Square:


    '''
    class square
    Args: side of the square
    '''
    def __init__(self, size=0):
        '''

        :param self:
        :param __size:
        :return:sides of square (__size)
        '''
        if (type(size)) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        '''multiply __size by itself to get square area'''
        a= self.__size * self.__size
        return a
    def size(self, value):
        ''' getting a self and modifying it'''

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
