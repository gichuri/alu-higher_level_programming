#!/usr/bin/python3
"""module to print a square using a particular pattern"""


def print_square(size):
    '''
   prints a square with a #
    checks if "size" is an int
    checks if "size" is a float and less than 0
    checks if "size" is less than 0
    checks if "size" is equal to 0
    '''
    if type(size) is not int or type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif size == 0:
        return None
    else:
        for i in range(size):
            for i in range(size):
                print('#', end=' ')
            print()
