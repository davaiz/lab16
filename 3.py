import sys
import os
for arg in sys.argv[1:]:
    file = open(arg, 'r')
    line = input.readline
    while line != '':
        line = input.readline
        print(line)
