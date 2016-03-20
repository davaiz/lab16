import sys
import os

for arg in sys.argv[1:]:
    filee = open('arg', 'r')
    line = filee.readline()
    while line:
        print (line)
        line = filee.readline()
