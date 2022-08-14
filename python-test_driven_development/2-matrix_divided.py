#!/usr/bin/python3
""" matrix_divided divides the given matrix
by the parameter "div", and returns the divided matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by "div"
    checks if the entire list is int/float
    checks if each list in the matrix are the same size
    checks if "div" is an int/float or is 0
    """
    mes0 = 'matrix must be a matrix (list of lists) of integers/floats'
    mes1 = 'Each row of the matrix must have the same size'
    inner_list = []
    res_list = []
    if not isinstance(div, (int,float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
       raise mes0
    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(mes0)
        if len(row) != len(matrix[0]):
            raise TypeError(mes1)
        else:
            for i in row:
                inner_list.append(round(i/div, 2))
                res_list.append(inner_list)

        return res_list

