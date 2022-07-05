#!/usr/bin/python3
def fizzbuzz():
    numbers = list(range(1, 101))
    for i in numbers:
        if i % 15 == 0 :
            print(i, 'FizzBuzz', end=' ')
        elif i % 3 == 0 :
            print (i ,'Fizz', end=' ')
        elif i % 5 == 0 :
            print(i , 'Buzz', end=' ')
        else:
            print(i , end=' ')
