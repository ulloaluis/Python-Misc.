#!/usr/bin/python

BANDIT24_PASS = 'REDACTED'

with open('pass.txt', 'w') as f:
    for i in range(10000):
        f.write(BANDIT24_PASS + ' %04d\n' % i)


# Short script used in a Bandit wargame on OverTheWire.
# Reads all 4 digit pins into a file, then passes it into 
# a port that has the functionality to read the file line 
# by line, stopping when the correct pincode is reached.

# Pre-condition: chmod +x brute1.py
# Usage: ./brute1.py
#        nc localhost 30002 << pass.txt
