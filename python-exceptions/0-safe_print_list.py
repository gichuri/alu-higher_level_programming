#!/usr/bin/python3
try:
    def safe_print_list(my_list=[], x=0):
        my_list2 = my_list[:x]
        count = 0
        for i in my_list2:
            count = count+1
         return my_list, count
except:
    print("Out of range")
