#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    original = tuple (my_list)
    if idx < 0 or idx >= len(my_list):
        print(original)
    else:
        my_list[idx] = element
        new_list = my_list
        print(new_list)
