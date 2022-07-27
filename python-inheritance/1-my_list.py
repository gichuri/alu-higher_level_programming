#!/usr/bin/python3

'''new subclass mylist 
    to extend builtin list'''


class Mylist(list):

    '''method to sort list'''

    def print_sorted(self):
        '''
        prints the sorted list
        '''
        print(sorted(self))
