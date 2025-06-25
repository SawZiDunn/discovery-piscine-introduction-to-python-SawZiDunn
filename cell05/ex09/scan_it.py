#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    search_string = sys.argv[2]
    matches = re.findall(re.escape(keyword), search_string)
    
    if matches:
        print(len(matches))
    else:
        print("none")