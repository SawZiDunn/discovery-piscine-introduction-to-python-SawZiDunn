#!/usr/bin/env python3

print("Enter a number")
number = int(input())

for i in range(10):
    result = i * number
    print(f"{i} x {number} = {result}")