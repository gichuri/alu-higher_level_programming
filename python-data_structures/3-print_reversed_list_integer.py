#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return
    else:
        def reverse(my_list):
            my_list.reverse()
            return my_list
        for i in reverse(my_list):
            print('{:d}'.format(i))
