#!/usr/bin/env python3

def add_one(x):
    x += 1
    return x

number = 10
print("Before calling add_one:", number)

add_one(number)

print("After calling add_one:", number)