#!/usr/bin/env python3

user_input = input()

result = ""

for char in user_input:
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char 

print(result)