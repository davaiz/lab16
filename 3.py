import sys
import os

for arg in sys.argv[1:]:
    with open('arg', 'r') as filee:
        line = filee.readline()
        while line:
            print (line)
            line = filee.readline()
