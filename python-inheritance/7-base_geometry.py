#!/usr/bin/python3

'''adding to geometry class'''


class BaseGeometry:
    '''new class as super class'''

    def area(self):

        '''method raise an exemption
                lack of implementation'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        '''validate value as int'''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
