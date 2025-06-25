#!/usr/bin/env python3

import sys

def main():
    
    if len(sys.argv) != 2:
        print("none")
        return
   
    parameter = sys.argv[1]
    print(parameter.upper())

if __name__ == "__main__":
    main()