#!/usr/bin/env python3

num = input("Give me a number: ")

try:
    number = float(num)
    if number == int(number):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("That's not a valid number.")