#!/usr/bin/env python3

print("Enter a number less than 25")
number = int(input())

if number > 25:
    print("Error")
else:
    while number <= 24:
        print(f"Inside the loop, my variable is {number}")
        number += 1
    print("Inside the loop, my variable is 25")