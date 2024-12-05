#!/usr/bin/python3
# 
# Create a script that accepts the file name and puts its extension to output. If there is no extension - an exception should be raised.

import sys

# I make an assumption that extension is what is after last dot in file name.

if '.' in sys.argv[1]:
    divided = sys.argv[1].split('.')
    print(divided[-1])
else: 
    raise Exception("There is no extention")