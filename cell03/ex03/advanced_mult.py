#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
else:
   
    table_number = 0
    while table_number <= 10:
    
        output = f"Table de {table_number}:"
        
       
        multiplier = 0
        while multiplier <= 10:
            result = table_number * multiplier
            output += f" {result}"
            multiplier += 1
        
       
        print(output)
        
     
        table_number += 1