#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif number % 10 == 0:
    print(f"Last digit of {number} is {num} and is 0")
elif num in range(1, 6):
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
