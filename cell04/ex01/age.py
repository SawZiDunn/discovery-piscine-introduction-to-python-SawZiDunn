#!/usr/bin/env python3

num = int(input("Please tell me your age: "))

print("You are currently", num ," years old.")

for i in range(10,40, 10):
    print("In" , i, "years, you'll be ", num + i, " years old.")  