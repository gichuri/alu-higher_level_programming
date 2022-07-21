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
    """initialisation of square
    attributes: size(int) defaults to zero if no value is passed
    """
            self.size = size

    def size(self):
        '''getter'''
        return self.__size

    def size(self, value):
        ''' getting a self and modifying it'''

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''multiply __size by itself to get square area'''
        a= (self.__size)**2
        return a
