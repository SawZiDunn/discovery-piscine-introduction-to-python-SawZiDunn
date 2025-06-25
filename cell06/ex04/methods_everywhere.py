#!/usr/bin/env python3

import sys

def shrink(text):
    
    print(text[:8])

def enlarge(text):
    
    result = text + 'Z' * (8 - len(text))
    print(result)

def main():
    if len(sys.argv) < 2:
        print("none")
        return
    
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)

if __name__ == "__main__":
    main()