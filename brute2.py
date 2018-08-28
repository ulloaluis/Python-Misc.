#!/usr/bin/python

import os

command = '~/leviathan6 '

for i in range(10000):
    os.system(command + ("%04d" % i))
    
# Short brute force script for 4 digit pin code
# Used in https://overthewire.org/wargames/leviathan/
# Pre-condition: chmod +x brute2.py
