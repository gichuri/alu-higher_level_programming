#!/usr/bin/python3

def safe_print_division(a, b):
   
    try:
        c = a/b 
        print('inside result: {}'.format(c))
    except ZeroDivisionError:
        return None 
    finally:
        if a and b > 0: 
            print("{} / {} = {}".format(a, b, c))
        else: 
            print('{} / {} = {}'.format(a, b, None))
