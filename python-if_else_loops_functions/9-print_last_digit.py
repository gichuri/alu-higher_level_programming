#!/usr/bin/python3
def print_last_digit(number):
    num = number % 10
    if number < 0:
        num= ((-1 * number) % 10) * -1
        print(num)
    else:
        print (num)
