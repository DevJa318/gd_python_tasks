#!/usr/bin/python3
# 
# Create a script that accepts the file name and puts its extension to output. If there is no extension - an exception should be raised.

import sys

## add try, except
# pytania ... ( za długo na linuxie.. )
## czy w tym przypadku nazwy mogą mieć kropkę w nazwie? 
## czy rozszerzenia mogą być dwuczłonowe?
## co jeśli ma kropki a nie ma rozszerzenia :S


if '.' in sys.argv[1]:
    divided = sys.argv[1].split('.')
    print(divided[-1])
else: 
    raise Exception("There is no extention")