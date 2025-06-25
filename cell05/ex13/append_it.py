#!/usr/bin/env python3

import sys
import re

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        if not re.search(r'ism$', arg):
            print(arg + "ism")