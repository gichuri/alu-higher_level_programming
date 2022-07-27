#!/usr/bin/python3
"""
function to read a file and print content to stdout
"""


def read_file(filename=""):
    '''use with to open and close file''' 

    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read())
