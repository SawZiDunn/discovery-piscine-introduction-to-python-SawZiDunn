#!/usr/bin/env python3

num =  input("Please enter a number: ")
    
try:
    num = float(num)
    if num == 0:
        print("This number is both positive and negative.")
    elif num < 0:
        print("This number is negative.")
    else:
        print("This number is positive.")
except ValueError:
    print("Please enter a valid number.")
