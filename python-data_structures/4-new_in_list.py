#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    original = tuple (my_list)
    if idx < 0 or idx >= len(my_list):
        return(original)
    else:
        my_list[idx] = element
        new_list = my_list
        return new_list
